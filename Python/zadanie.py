'''x=input("podaj napis")
if x==x[::-1]:
    print("słowo jest palindromem")
else:
    print("słowo nie jest palindromem")'''

x=input("podaj napis")
z=len(x)
for y in range(len(x)//2):
    if x[y] !=x[z-y-1]:
        print("False")
    else:
        print("True")