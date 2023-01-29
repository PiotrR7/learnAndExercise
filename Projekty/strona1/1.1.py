print("podaj wartość zmiennej a")
a=input()
print("podaj wartość zmiennej b")
b=input()
print("podaj wartość zmiennej c")
c=input()
print(a,b,c)
print(int(a)+int(b)+int(c))
delta=int(b)*int(b)-4*int(a)*int(c)
print(delta)
print("delta wynosi",delta)
if(delta>0):
    print("2 rozwiązania")
if(delta==0):
    print("1 rozwiązanie")
if(delta<0):
    print("brak rozwiązań")