kontakty ={
    "Piotr":600123456,
    "Tomek":600123457,
    "Jacek":600123458,
}

for imie,numer in kontakty.items():
    print(imie,kontakty)

def sprawdz(x):
    print(kontakty[x])

sprawdz('Jacek')
usable_range = kontakty.__len__()

y=True
while y == True:
    y=input(': ')
    if y == 0:
        print('goodbaye')
        break
    if y not in kontakty:
        print('wprowadziłeś złe dane')
        y = True
    else:
        sprawdz(y)
        y = True