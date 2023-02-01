with open('cyfry_pi.txt','r') as file_object:
    contens=file_object.read()
    print(contens.rstrip())
    print(contens.lstrip())