def silnia(n): return n*silnia(n-1) if n>1 else 1

print(silnia(1))
print(silnia(5))
print(silnia(7))