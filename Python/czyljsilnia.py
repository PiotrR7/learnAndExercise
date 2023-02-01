import re
liczby=[]
plik=open('liczby_silania.txt.txt').readline()
liczby=plik.split()


# print(liczby)
silnie=['1,','6,','24,','120,','720,']

print(len(liczby))
for x in range(0,len(liczby)):
    if liczby[x] in silnie:
        print(silnie[x],"                  ok            ")