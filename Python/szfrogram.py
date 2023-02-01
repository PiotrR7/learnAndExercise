a=input('podaj wyraz: ')
b=int(input('podaj klucz: '))
tablica=[]
zaszyfrowany_wyraz=[]
for x in range(len(a)):
    tablica.append(a[x])
print(tablica)

for y in(tablica):
    c=ord(tablica[y])+b
    if int(c)>122:
        c=int(c)-122*(int(c)//122)-26
        d=chr(c)
    zaszyfrowany_wyraz.append(d)

print(zaszyfrowany_wyraz)
    








# a=input(': ')
# b=(ord(a))
# c=(ord(a)+2)
# d=(chr(c))
# print(d.upper())
# print(d.lower())