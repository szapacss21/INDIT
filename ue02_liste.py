meine_liste = ["ich bin", "ein", "string in einer" , "liste"]
zahlenliste = [1,2,3,43,7,2]

for element in meine_liste:
    print(element)
    
    
teilliste = zahlenliste
print(teilliste)

string = "abcdef"
mybytes = bytearray(string)
mybytes[1] = "y"
string = str(mybytes)
print(string)
