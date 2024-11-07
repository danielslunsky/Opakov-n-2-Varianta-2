#1
rady = ["Eanos", "Eas", "Falls", "Zagz", "Sggrss", "Eacs"]
for rada in rady:
    print(f"Řada vozidla {rada}")
#2
text=0
zadana_cisla=0

while True:
    text=(input("Zadej hodnotu: "))
    zadana_cisla = zadana_cisla + 1
    if text == "stop":
        print("Počet zadaných čísel: ", zadana_cisla)
        break

    else:
        print("Zadaná hodnota: ", text)

#3
mesic=(int(input("Zadejte hodnotu od 1 do 12(měsíce): ")))

if mesic > 2 and mesic < 6:
    print("Jaro")
elif mesic > 5 and mesic < 9:
    print("Léto")
elif mesic > 8 and mesic < 12:
    print("Podzim")
if mesic == 12 or mesic > 0 and mesic < 3:
    print("Zima")

#4
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
    {'name': 'Antigua and Barbuda', 'capital': "Saint John's", 'region': 'Americas', 'subregion': 'Caribbean', 'population': 86295, 'area': 442.0},
    {'name': 'Bahamas', 'capital': 'Nassau', 'region': 'Americas', 'subregion': 'Caribbean', 'population': 378040, 'area': 13943.0},
    {'name': 'Bahrain', 'capital': 'Manama', 'region': 'Asia', 'subregion': 'Western Asia', 'population': 1404900,'area': 765.0},
]
pocet_statu_europe = 0
celkova_rozloha_europe = 0
oceania_nazvy = []
for stat in staty:
    if stat['region'] == "Europe":
        pocet_statu_europe += 1
        celkova_rozloha_europe += stat['area']
    if stat['region'] == "Oceania":
        oceania_nazvy.append(stat['name'])

print("Počet států v Evropě:", pocet_statu_europe)
print("Celková rozloha států v Evropě:", celkova_rozloha_europe)
print("Státy v regionu Oceania:", oceania_nazvy)






