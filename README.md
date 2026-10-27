📊 Analýza docházky

Konzolová aplikace v Pythonu pro analýzu zaměstnanecké docházky.

Projekt zpracovává data z docházkového systému, vypočítává statistiky zaměstnanců a vytváří přehledné výstupy pro lepší orientaci v odpracované době.

✨ Funkce
📁 Načítání docházky ze souboru CSV.
⏱️ Výpočet délky směn, celkové odpracované doby a průměrné délky směny.
🏆 Žebříček zaměstnanců podle odpracovaných hodin.
📅 Denní statistiky příchodů a odchodů.
🔎 Vyhledávání zaměstnanců podle jména nebo čísla čipu.
⚠️ Kontrola pozdních příchodů a krátkých směn.
💾 Export výsledků do formátu JSON.
🎨 Přehlednější výpisy v terminálu pomocí knihovny Rich.
🛠️ Použité technologie
Python 3
Rich – formátování výstupu v terminálu
CSV – načítání vstupních dat
JSON – ukládání výsledků
datetime – práce s datem a časem
collections a pathlib – zpracování dat a práce se soubory
🚀 Instalace
1. Naklonování repozitáře
powershell
git clone https://github.com/JakubDr/analyza-dochazky.git
cd analyza-dochazky

2. Vytvoření virtuálního prostředí
powershell
py -m venv .venv

3. Aktivace virtuálního prostředí
powershell
.\.venv\Scripts\Activate.ps1

4. Instalace knihoven
powershell
python -m pip install -r requirements.txt

▶️ Spuštění aplikace

Připrav CSV soubor s docházkovými záznamy a spusť:

powershell
python dochazka.py dochazka.csv


Název vstupního souboru lze změnit podle potřeby.

Po spuštění se zobrazí konzolové menu, ve kterém si uživatel vybere požadovanou analýzu.

📂 Struktura projektu
text
analyza-dochazky/
├── dochazka.py
├── requirements.txt
├── .gitignore
├── README.md
├── dochazka.csv
└── vysledek.json

Soubor	Popis
dochazka.py	Hlavní zdrojový kód aplikace
requirements.txt	Seznam potřebných knihoven
.gitignore	Soubory, které se nemají nahrávat do Gitu
README.md	Dokumentace projektu
dochazka.csv	Vstupní data
vysledek.json	Exportované výsledky analýzy
📄 Formát vstupních dat

Vstupní CSV obsahuje následující údaje:

Sloupec	Význam
Číslo čipu	Identifikátor zaměstnance
Zaměstnanec	Jméno zaměstnance
Příchod	Datum a čas příchodu
Odchod	Datum a čas odchodu

Podporované formáty data a času zahrnují například:

text
12.10.2026 7:02
2026-10-12 07:02


Každý řádek představuje jeden pobyt zaměstnance na pracovišti.

📈 Výstup analýzy

Aplikace dokáže vytvořit přehled odpracovaných hodin jednotlivých zaměstnanců, denní statistiky a seznam zaznamenaných směn.

Výsledky lze uložit do souboru vysledek.json a dále využít pro zpracování nebo přehledné uchování statistik.

Poznámka: Délka směny se počítá jako rozdíl mezi příchodem a odchodem. Bez dalších údajů aplikace automaticky neodečítá přestávky a neurčuje skutečně placenou pracovní dobu.

🔒 Ochrana osobních údajů

Docházková data mohou obsahovat osobní údaje zaměstnanců. Do veřejného repozitáře proto nepatří skutečné firemní záznamy ani exporty obsahující osobní údaje. Pro demonstraci aplikace používejte anonymizovaná ukázková data.

🎯 Cíl projektu

Cílem projektu je procvičit práci s CSV a JSON, funkcemi, seznamy, slovníky, podmínkami, cykly a datem a časem v Pythonu a vytvořit praktický nástroj pro analýzu docházkových údajů.

👨‍💻 Autor

JakubDr

Školní projekt – programování v Pythonu.
