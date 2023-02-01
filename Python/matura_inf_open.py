tablica=[]
sciezka='przyklad.txt'

with open(sciezka) as f:
    for line in f:
        tablica.append(line)
print(len(tablica))

if(tablica[0]=='D'):
    print(tablica[0]+tablica[1])