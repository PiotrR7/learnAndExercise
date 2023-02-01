f = open('przyklad.txt')

tablica = []

for y in range(0, len(open("przyklad.txt").readlines())):
    tablica.append(f.readline())

for x in range(0,len(tablica)):
    if len(tablica[x])>9:
        print(tablica[x][9],end="")