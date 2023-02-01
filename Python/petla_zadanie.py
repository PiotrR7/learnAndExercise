#     def kodowanie():
#     a=input("podaj litere: ")
#     b=int(input("podaj klucz: "))
#     c=int(ord(a))
#     d=c+b
#     e=(chr(d))
#     print(e)

# kodowanie()



def kodowanie_wyrazu():
    a=input("podaj wyraz: ")
    b=int(input("podaj klucz: "))
    # literowanie wyrazu
    for c in range(0,len(a)):
        int(ord(c))
    # 

    

kodowanie_wyrazu()


# 1)zamień pobrazy napis na małe litery
# 2)przy zamianie na liczbę są dwa przypadki
#   jeżeli liczba+klucz jest większa od 123 to liczba -97
#   jeżeli liczba+klucz jest mniejsza od 97 to liczba +26