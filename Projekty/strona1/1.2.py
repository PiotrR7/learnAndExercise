print("podaj imię")
imie=input()
print("podaj wiek")
wiek=input()
print(imie,wiek)
pozostalo=(100-int(wiek))
print("do 100 lat zostało ci",pozostalo,"lat")
if(pozostalo>82):
    print("idź po mleko i idź spać")
if(pozostalo==82):
    print("witamy w gronie dorosłych")
if(pozostalo<82):
    print("stawiasz następną kolejkę")