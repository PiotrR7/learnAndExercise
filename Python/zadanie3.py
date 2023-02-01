from random import randrange
import datetime

x = datetime.datetime.now()
x = x.strftime('%d')

# funkcja witaj

def witaj():
    print('Dzień dobry')

# tablica cytaty

plik = open('cytatymotywacyjne.txt',encoding="utf-8")
cytaty= plik.readlines()

if x == '09':
    print(cytaty[8])

if x[0] == 0:
    print(cytaty[x[1]])
else:
    print(cytaty[x])