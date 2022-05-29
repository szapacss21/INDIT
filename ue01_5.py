print("Ist das Wetter Sonnig bitte 1 eingeben")
print("Ist das Wetter regnerisch bitte 2 eingeben")

strWetter = input("Wie wird das Wetter?: ")
floatWetter = float(strWetter)


if floatWetter == 1:
    print("Die Party findet draussen statt")
elif floatWetter == 2:
    print("Die Party findet im Keller statt")
else:
    print("Falsche Eingabe bitte Wetter korrekt eingeben")