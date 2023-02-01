# import re

# dopasowanie = wilk.search('Nosił wilk razy kilka, ponieśli i wilka.')
# print('Początek:                {}'.format(dopasowanie.start()))
# print('Koniec:                  {}'.format(dopasowanie.end()))
# print('Krotka początku i końca: {}'.format(dopasowanie.span()))
# print('Dopasowany tekst:        {}'.format(dopasowanie.group()))

import re

tekst = """Wyobraz sobie, ze ten tekst zawiera numer
PIN 9434 twojej karty do bankomatu, a ty wlasnie go
zapomniales. Jak szybko go odnalezc?"""

sciezka = r'\d\d\d\d'
dopasowanie = re.search(sciezka, tekst)

if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
    numer = dopasowanie.group()
    print(numer)