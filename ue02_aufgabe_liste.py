woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

strWort = input("Bitte geben sie ein Wort zum Übersetzen ein: ") # Wort eingeben

#vergleichen ob das Wort vorkommt
inti = 0
max = len(woerterbuch_deutsch)

while inti <= max-1:
    if woerterbuch_deutsch[inti] == strWort:
        print(woerterbuch_englisch[inti])
              break
              init += 1


    