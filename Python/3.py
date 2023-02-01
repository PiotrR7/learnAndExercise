import re

plik=open('instrukcje.txt','r+')
print(plik.read())
plik.close()

d=r'DOPISZ'
sd=re.findall(d,plik)

u=r'USUN'
su=re.findall(u,plik)


dlugosc=0
if sd:
    długość += 1
elif su:
    długość -= 1