# PVA2 - Programování a vývoj aplikací
## Opakování 2: Varianta 2

Čas na odevzdání: 45 minut. Rozhodným časem je čas na githubu.


**Soubory uložte a odešlete do repozitáře**
Řešení, které nebude přístupné v repozitáři je považováno jako neodevzdané.

Řešení vypracujte do souboru `reseni.py`. 


## Obsah

### 1. Cyklus (3b)
Do seznamu řady přidejte prvek Eacs a pomocí cyklu zobrazte všechny prvky ve tvaru `Řada vozidla ???`

`rady = ["Eanos", "Eas", "Falls", "Zagz", "Sggrss"]`

### 2. Cyklus (6b)

Naprogramujte cyklus, který bude po uživateli chtít zadávat čísla tak dlouho, dokud text `stop`. Zadanou hodnotu zobrazte uživateli v podobě `Zadaná hodnota: ???.`.
Pokud je zadána text `stop`, dojde k přerušení zpracování a zobrazení počtu zadaných čísel.


### 3. Podmínka (8b)

Mějme proměnnou `mesic`, která může nabývat hodnot 1-12, kdy leden je reprezentován 1 a prosinec 12. Hodnotu čísla měsíce si vyžádejte od uživatele. Deklarujte podmínku přesně dle zadání, která bude vyhodnocovat vstupy:
* hodnoty pro březen až květen zobrazte jaro
* hodnoty pro červen až srpen zobrazte léto
* hodnoty pro září až listopad zobrazte podzim
* hodnoty pro prosinec až únor zobrazte zima
* bude-li vložená jiná hodnota, zobrazte uživateli "nepodporovaný vstup"

### 4. Řídící struktury (8 bodů)

Za využití cyklu a níže uvedeného seznamu slovníku `staty` (2b)
* spočítej počet států (2b)
* spočítej celkovou rozlohu států (`area`) z regionu `Europe`. (2b)
* vypiš názvy států z regionu `Oceania` (2b)

```
staty = [
    {'name': 'Afghanistan', 'capital': 'Kabul', 'region': 'Asia', 'subregion': 'Southern Asia', 'population': 27657145, 'area': 652230.0, 'gini': 27.8},
    {'name': 'Åland Islands', 'capital': 'Mariehamn', 'region': 'Europe', 'subregion': 'Northern Europe', 'population': 28875, 'area': 1580.0},
    {'name': 'Albania', 'capital': 'Tirana', 'region': 'Europe', 'subregion': 'Southern Europe', 'population': 2886026, 'area': 28748.0, 'gini': 34.5},
    {'name': 'Algeria', 'capital': 'Algiers', 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 40400000, 'area': 2381741.0, 'gini': 35.3},
    {'name': 'American Samoa', 'capital': 'Pago Pago', 'region': 'Oceania', 'subregion': 'Polynesia', 'population': 57100, 'area': 199.0},
    {'name': 'Andorra', 'capital': 'Andorra la Vella', 'region': 'Europe', 'subregion': 'Southern Europe', 'population': 78014, 'area': 468.0},
    {'name': 'Angola', 'capital': 'Luanda', 'region': 'Africa', 'subregion': 'Middle Africa', 'population': 25868000, 'area': 1246700.0, 'gini': 58.6},
    {'name': 'Anguilla', 'capital': 'The Valley', 'region': 'Americas', 'subregion': 'Caribbean', 'population': 13452, 'area': 91.0},
    {'name': 'Antarctica', 'capital': '', 'region': 'Polar', 'subregion': '', 'population': 1000, 'area': 14000000.0},
    {'name': 'Antigua and Barbuda', 'capital': "Saint John's", 'region': 'Americas', 'subregion': 'Caribbean', 'population': 86295, 'area': 442.0}
    {'name': 'Bahamas', 'capital': 'Nassau', 'region': 'Americas', 'subregion': 'Caribbean', 'population': 378040, 'area': 13943.0},
    {'name': 'Bahrain', 'capital': 'Manama', 'region': 'Asia', 'subregion': 'Western Asia', 'population': 1404900,'area': 765.0},
    ]
```
