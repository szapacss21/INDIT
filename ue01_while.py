# whileSchleife
#
#while [Bedingung] :
#    Anweisungsblock

intZaehler = 0
intReihensumme = 0

while intZaehler < 10:
    intZaehler += 1                 #entspricht intZaehler = intZaehler + 1
    print(intZaehler)
    intReihensumme += intZaehler    # entspricht inReihensumme = intReihensumme + intZaehler
    print(intReihensumme)

print("Reihensumme v, 1 bis 10: ", intReihensumme) 
