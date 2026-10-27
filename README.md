# 📊 Analýza docházky

Konzolová aplikace v Pythonu pro analýzu zaměstnanecké docházky.

Aplikace zpracovává data z docházkového systému, počítá statistiky zaměstnanců a vytváří přehledy odpracované doby.

## ✨ Funkce

* Načítání dat z CSV
* Výpočet délky směn a celkové odpracované doby
* Žebříček zaměstnanců podle odpracovaných hodin
* Denní statistiky příchodů a odchodů
* Vyhledávání podle jména nebo čísla čipu
* Kontrola pozdních příchodů a krátkých směn
* Export výsledků do JSON
* Přehlednější terminálové rozhraní pomocí Rich

## 🛠️ Technologie

* **Python 3**
* **Rich**
* **CSV a JSON**
* **datetime**
* **pathlib**
* **collections**

## 🚀 Instalace

1. **Naklonování repozitáře:**
   ```powershell
   git clone https://github.com/JakubDr/analyza-dochazky.git
   cd analyza-dochazky
   ```

2. **Vytvoření virtuálního prostředí:**
   ```powershell
   py -m venv .venv
   ```

3. **Aktivace prostředí ve Windows PowerShellu:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. **Instalace závislostí:**
   ```powershell
   python -m pip install -r requirements.txt
   ```

## ▶️ Spuštění

```powershell
python dochazka.py dochazka.csv
```

*Název vstupního souboru lze změnit podle potřeby.*

## 📂 Struktura projektu

```text
analyza-dochazky/
├── dochazka.py
├── requirements.txt
├── .gitignore
├── README.md
├── dochazka.csv
└── vysledek.json
```

| Soubor | Popis |
| :--- | :--- |
| `dochazka.py` | Hlavní program |
| `requirements.txt` | Potřebné knihovny |
| `.gitignore` | Ignorované soubory |
| `README.md` | Dokumentace |
| `dochazka.csv` | Vstupní data |
| `vysledek.json` | Exportované výsledky |

## 📄 Vstupní data

CSV obsahuje čtyři sloupce:
* Číslo čipu
* Zaměstnanec
* Příchod
* Odchod

Podporované formáty data a času zahrnují například:
* `12.10.2026 7:02`
* `2026-10-12 07:02`

Každý řádek představuje jeden pobyt zaměstnance na pracovišti.

## 📈 Výstupy

Program vypočítává odpracované hodiny, průměrnou délku směny, denní statistiky a přehled jednotlivých záznamů. Výsledky lze exportovat do JSON.

> 💡 **Poznámka:** Délka směny se počítá jako rozdíl mezi příchodem a odchodem. Přestávky se automaticky neodečítají.

## 🔒 Ochrana osobních údajů

Do veřejného repozitáře nepatří skutečná docházková data zaměstnanců. Pro ukázky používejte anonymizovaná data.

## 🎯 Cíl projektu

Cílem je procvičit práci se soubory CSV a JSON, funkcemi, seznamy, slovníky, podmínkami, cykly a datem a časem v Pythonu.

## 👨‍💻 Autor

* **Jakub Drastík a Michael Mička**
* Školní projekt – programování v Pythonu.
