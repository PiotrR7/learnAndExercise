sciezka = 'cyfry_pi.txt'
with open(sciezka) as f:
    lista = f.readlines()

for wiersz in lista:
    print(wiersz.rstrip())