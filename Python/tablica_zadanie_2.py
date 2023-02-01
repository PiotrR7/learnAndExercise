tab1=["Ala","Ola","Tola","Basia"]
tab1.append("Kasia")
tab1.append("Lena")
tab1.append("Asia")
tab1.append("Julia")
tab1.append("Zuzanna")
tab1.append("Zofia")
print(tab1)

tab2=[]
tab2.append("Antoni")
tab2.append("Jakub")
tab2.append("Jan")
tab2.append("Szymon")
tab2.append("Franciszek")
print(tab2)

imiona=[]
imiona.extend(tab1)
imiona.extend(tab2)
print(imiona)

imiona.sort()
print(imiona)