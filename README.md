📊 Analýza docházky

Konzolová aplikace v Pythonu pro zpracování a vyhodnocování zaměstnanecké docházky.

Aplikace načítá záznamy z CSV souboru, vypočítává statistiky zaměstnanců a umožňuje vedení firmy získat přehled o odpracované době, příchodech a délce směn.

✨ Funkce
📁 Načítání dat – podpora CSV souborů se středníkem nebo tabulátorem jako oddělovačem.
⏱️ Výpočet odpracované doby – délka jednotlivých směn, celkový počet hodin a průměrná délka směny.
🏆 Žebříček zaměstnanců – seřazení podle celkové odpracované doby.
📅 Denní statistiky – první příchod, poslední odchod a průměrná délka směny.
🔎 Vyhledávání – nalezení zaměstnance podle jména nebo čísla čipu.
⚠️ Kontrola docházky – upozornění na pozdní příchody a neobvykle krátké směny.
💾 Export do JSON – uložení souhrnných statistik a zpracovaných záznamů.
🎨 Terminálové rozhraní – přehlednější výpisy pomocí knihovny Rich.
🛠️ Použité technologie
Python 3
Rich
CSV a JSON
datetime, collections, pathlib
🚀 Instalace a spuštění
1. Naklonování projektu
bash
git clone https://github.com/JakubDr/analyza-dochazky.git
cd analyza-dochazky

2. Vytvoření virtuálního prostředí

Windows – PowerShell:

powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Instalace závislostí
powershell
python -m pip install -r requirements.txt

4. Spuštění aplikace

Do složky projektu vlož vstupní CSV soubor a spusť:

powershell
python dochazka.py dochazka.csv


Aplikace následně zobrazí konzolové menu, ze kterého lze vybírat jednotlivé analýzy.

📂 Struktura projektu
text
analyza-dochazky/
├── dochazka.py       # Hlavní program
├── dochazka.csv      # Vstupní data (lokální nebo ukázková)
├── requirements.txt  # Závislosti projektu
├── .gitignore        # Ignorované soubory
├── README.md         # Dokumentace
└── vysledek.json     # Exportované výsledky

📄 Formát vstupních dat

CSV soubor obsahuje čtyři sloupce:

Sloupec	Význam
číslo čipu	Jedinečný identifikátor zaměstnance
zaměstnanec	Jméno zaměstnance
příchod	Datum a čas příchodu
odchod	Datum a čas odchodu

Aplikace podporuje například tyto formáty data a času:

12.10.2026 7:02
2026-10-12 07:02

Každý řádek představuje jeden pobyt zaměstnance na pracovišti.

💡 Výstup a využití

Zpracované výsledky lze exportovat do souboru vysledek.json. Obsahují souhrny za zaměstnance, denní statistiky a jednotlivé směny.

Výsledky mohou pomoci například při:

porovnávání odpracované doby zaměstnanců,
sledování docházkových trendů,
hledání neobvyklých záznamů,
získávání souhrnných podkladů pro vedení firmy.

Poznámka: Délka směny se počítá z rozdílu mezi příchodem a odchodem. Bez dalších údajů aplikace automaticky neodečítá přestávky ani neurčuje skutečně placenou pracovní dobu.

🔒 Ochrana dat

Docházková data mohou obsahovat osobní údaje. Do veřejného repozitáře proto nepatří skutečné firemní záznamy ani exporty obsahující osobní údaje. Pro ukázky používejte anonymizovaná data.

👨‍💻 Autor

Jakub Drastík
Michael Mička

Školní projekt – zpracování a analýza dat v Pythonu.