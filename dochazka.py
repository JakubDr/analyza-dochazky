
import csv
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

console = Console()
POZDE = "08:00"
MIN_SMENA = 6
MAX_SMENA = 12


def preved_cas(text):
    for format_casu in ("%d.%m.%Y %H:%M", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(text.strip(), format_casu)
        except ValueError:
            pass
    raise ValueError(f"Spatny datum: {text}")


def nacti_data(cesta):
    zaznamy = []
    chyby = 0

    with open(cesta, encoding="utf-8-sig", newline="") as soubor:
        prvni = soubor.readline()
        if not prvni:
            raise ValueError("Soubor je prazdny.")

        oddelovac = "\t" if prvni.count("\t") > prvni.count(";") else ";"
        soubor.seek(0)
        ctecka = csv.reader(soubor, delimiter=oddelovac)
        hlavicka = next(ctecka, [])

        hlavicka = [x.strip().casefold() for x in hlavicka]
        varianty = [
            ("cislo cipu", "číslo čipu", "cip", "čip", "cislo_cipu"),
            ("zamestnanec", "zaměstnanec", "jmeno", "jméno"),
            ("prichod", "příchod"),
            ("odchod",)
        ]

        indexy = []
        for moznosti in varianty:
            index = next(
                (i for i, x in enumerate(hlavicka) if x in moznosti),
                None
            )
            if index is None:
                raise ValueError("CSV musi obsahovat cip, zamestnance, prichod a odchod.")
            indexy.append(index)

        for cislo, radek in enumerate(ctecka, 2):
            try:
                cip, jmeno, prichod, odchod = [
                    radek[i].strip() for i in indexy
                ]
                prichod = preved_cas(prichod)
                odchod = preved_cas(odchod)

                if not cip or not jmeno or odchod <= prichod:
                    raise ValueError("Neplatny zaznam.")

                hodiny = (odchod - prichod).total_seconds() / 3600

                zaznamy.append({
                    "cip": cip,
                    "jmeno": jmeno,
                    "prichod": prichod,
                    "odchod": odchod,
                    "datum": prichod.date().isoformat(),
                    "hodiny": round(hodiny, 2)
                })
            except (ValueError, IndexError):
                chyby += 1
                console.print(f"Radek {cislo} preskocen.", style="yellow")

    if not zaznamy:
        raise ValueError("Nebyly nalezeny platne zaznamy.")

    return zaznamy, chyby


def statistiky(zaznamy):
    osoby = {}

    for z in zaznamy:
        cip = z["cip"]
        if cip not in osoby:
            osoby[cip] = {
                "cip": cip, "jmeno": z["jmeno"], "smeny": [],
                "celkem": 0
            }
        osoby[cip]["smeny"].append(z)
        osoby[cip]["celkem"] += z["hodiny"]

    for o in osoby.values():
        o["pocet"] = len(o["smeny"])
        o["celkem"] = round(o["celkem"], 2)
        o["prumer"] = round(o["celkem"] / o["pocet"], 2)

    return osoby


def tabulka(nazev, sloupce, radky):
    t = Table(title=nazev, box=box.ROUNDED, show_lines=True)
    for s in sloupce:
        t.add_column(s)
    for radek in radky:
        t.add_row(*[str(x) for x in radek])
    console.print(t)


def prehled(zaznamy, osoby, chyby):
    prvni = min(zaznamy, key=lambda z: z["prichod"])
    posledni = max(zaznamy, key=lambda z: z["odchod"])

    console.print(Panel("[bold cyan]PREHLED DOCHAZKY[/bold cyan]"))
    tabulka("Celkovy prehled", ["Ukazatel", "Hodnota"], [
        ("Pocet zaznamu", len(zaznamy)),
        ("Zamestnanci", len(osoby)),
        ("Dny", len(set(z["datum"] for z in zaznamy))),
        ("Celkem hodin", f"{sum(z['hodiny'] for z in zaznamy):.2f}"),
        ("Chybne radky", chyby),
        ("Prvni prichod", f"{prvni['jmeno']} {prvni['prichod']:%d.%m.%Y %H:%M}"),
        ("Posledni odchod", f"{posledni['jmeno']} {posledni['odchod']:%d.%m.%Y %H:%M}")
    ])


def zebricek(osoby):
    serazeni = sorted(osoby.values(), key=lambda o: o["celkem"], reverse=True)
    tabulka("Zebricek zamestnancu",
            ["Cip", "Zamestnanec", "Smeny", "Celkem h", "Prumer h"],
            [(o["cip"], o["jmeno"], o["pocet"], o["celkem"], o["prumer"])
             for o in serazeni])


def denni_statistiky(zaznamy):
    dny = defaultdict(list)
    for z in zaznamy:
        dny[z["datum"]].append(z)

    radky = []
    for datum, smeny in sorted(dny.items()):
        prvni = min(smeny, key=lambda z: z["prichod"])
        posledni = max(smeny, key=lambda z: z["odchod"])
        radky.append((
            datum, len(smeny),
            f"{prvni['jmeno']} {prvni['prichod']:%H:%M}",
            f"{posledni['jmeno']} {posledni['odchod']:%H:%M}",
            round(sum(z["hodiny"] for z in smeny) / len(smeny), 2),
            round(sum(z["hodiny"] for z in smeny), 2)
        ))

    tabulka("Denni statistiky",
            ["Datum", "Smeny", "Prvni prichod", "Posledni odchod",
             "Prumer h", "Celkem h"], radky)


def vyhledavani(zaznamy):
    dotaz = Prompt.ask("Zadej jmeno nebo cislo cipu").strip().casefold()
    nalezene = [z for z in zaznamy
                if dotaz and (dotaz in z["jmeno"].casefold()
                              or dotaz in z["cip"].casefold())]

    tabulka("Nalezene smeny",
            ["Datum", "Cip", "Zamestnanec", "Prichod", "Odchod", "Hodiny"],
            [(z["datum"], z["cip"], z["jmeno"],
              z["prichod"].strftime("%H:%M"),
              z["odchod"].strftime("%H:%M"), z["hodiny"])
             for z in nalezene])

    console.print(f"Celkem hodin: {sum(z['hodiny'] for z in nalezene):.2f}")


def filtr_data(zaznamy):
    try:
        od = datetime.strptime(Prompt.ask("Datum od (DD.MM.RRRR)"), "%d.%m.%Y").date()
        do = datetime.strptime(Prompt.ask("Datum do (DD.MM.RRRR)"), "%d.%m.%Y").date()
        if do < od:
            raise ValueError
    except ValueError:
        console.print("[red]Neplatna data.[/red]")
        return

    vyber = [z for z in zaznamy if od <= z["prichod"].date() <= do]
    tabulka("Smeny ve vybranem obdobi",
            ["Datum", "Zamestnanec", "Prichod", "Odchod", "Hodiny"],
            [(z["datum"], z["jmeno"], z["prichod"].strftime("%H:%M"),
              z["odchod"].strftime("%H:%M"), z["hodiny"]) for z in vyber])
    console.print(f"Pocet smen: {len(vyber)}")


def kontrola(zaznamy):
    pozdni = [z for z in zaznamy if z["prichod"].strftime("%H:%M") > POZDE]
    kratke = [z for z in zaznamy if z["hodiny"] < MIN_SMENA]
    dlouhe = [z for z in zaznamy if z["hodiny"] > MAX_SMENA]

    for nazev, seznam in [
        ("Pozdni prichody", pozdni),
        ("Kratke smeny", kratke),
        ("Dlouhe smeny", dlouhe)
    ]:
        tabulka(nazev, ["Datum", "Zamestnanec", "Prichod", "Odchod", "Hodin"],
                [(z["datum"], z["jmeno"], z["prichod"].strftime("%H:%M"),
                  z["odchod"].strftime("%H:%M"), z["hodiny"]) for z in seznam])

    console.print("[yellow]Upozorneni jsou orientacni, prestavky se neodecitaji.[/yellow]")


def export_json(zaznamy, osoby, cesta):
    vystup = {
        "zdroj": Path(cesta).name,
        "pocet_zaznamu": len(zaznamy),
        "pocet_zamestnancu": len(osoby),
        "celkem_hodin": round(sum(z["hodiny"] for z in zaznamy), 2),
        "zamestnanci": [
            {"cislo_cipu": o["cip"], "zamestnanec": o["jmeno"],
             "pocet_smen": o["pocet"], "celkem_hodin": o["celkem"],
             "prumerna_smena": o["prumer"]}
            for o in sorted(osoby.values(), key=lambda x: x["celkem"], reverse=True)
        ],
        "smeny": [
            {"cislo_cipu": z["cip"], "zamestnanec": z["jmeno"],
             "datum": z["datum"],
             "prichod": z["prichod"].strftime("%Y-%m-%d %H:%M"),
             "odchod": z["odchod"].strftime("%Y-%m-%d %H:%M"),
             "hodiny": z["hodiny"]}
            for z in zaznamy
        ]
    }

    nazev = Prompt.ask("Nazev JSON souboru", default="vysledek.json")
    try:
        with open(nazev, "w", encoding="utf-8") as soubor:
            json.dump(vystup, soubor, ensure_ascii=False, indent=4)
        console.print(f"[green]Ulozeno do {Path(nazev).resolve()}[/green]")
    except OSError as chyba:
        console.print(f"[red]Chyba pri ukladani: {chyba}[/red]")


def main():
    if len(sys.argv) < 2:
        console.print("Pouziti: python dochazka.py dochazka.csv", style="red")
        return

    cesta = Path(sys.argv[1])
    if not cesta.is_file():
        console.print(f"Soubor nenalezen: {cesta}", style="red")
        return

    try:
        zaznamy, chyby = nacti_data(cesta)
    except (OSError, ValueError, csv.Error) as chyba:
        console.print(f"Chyba: {chyba}", style="red")
        return

    osoby = statistiky(zaznamy)
    console.print(Panel(
        f"Nacteno smen: {len(zaznamy)} | Zamestnancu: {len(osoby)} | Chyb: {chyby}",
        title="Dochazka", border_style="green"
    ))

    while True:
        console.print(Panel(
            "[1] Celkovy prehled\n"
            "[2] Zebricek zamestnancu\n"
            "[3] Denni statistiky\n"
            "[4] Vyhledavani\n"
            "[5] Filtrovani podle data\n"
            "[6] Kontrola dochazky\n"
            "[7] Export do JSON\n"
            "[0] Konec",
            title="ANALYZA DOCHAZKY", border_style="cyan"
        ))

        volba = Prompt.ask("Vyber", choices=["0", "1", "2", "3", "4", "5", "6", "7"])

        if volba == "1":
            prehled(zaznamy, osoby, chyby)
        elif volba == "2":
            zebricek(osoby)
        elif volba == "3":
            denni_statistiky(zaznamy)
        elif volba == "4":
            vyhledavani(zaznamy)
        elif volba == "5":
            filtr_data(zaznamy)
        elif volba == "6":
            kontrola(zaznamy)
        elif volba == "7":
            export_json(zaznamy, osoby, cesta)
        elif volba == "0":
            console.print("[bold green]Program ukoncen.[/bold green]")
            break


if __name__ == "__main__":
    main()
