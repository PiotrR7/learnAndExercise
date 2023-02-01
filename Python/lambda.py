# lista = [1,3,5,7]
# from functools import reduce
# print(f"Nasza lista: {lista}\n")
# print(f"Przykład zastosowania map: {list( map(lambda _: _*2, lista) )}")
# print(f"Przykład zastosowania filter: {list( filter(lambda _: _>3, lista) )}")
# print(f"Przykład zastosowania reduce: { reduce(lambda x,y: x+y, lista) }")

a = lambda x : x + 10
b = lambda x : x - 10
c = lambda x : x * 10
d = lambda x : x / 10

print(a(10))
print(b(10))
print(c(10))
print(d(10))