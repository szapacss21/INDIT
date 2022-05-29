drinks = {"Klaus" : "Bier",
          "Silvia" : "Wein",
          "ET" : "Whisky"}
name = input("Name: ")

if name in drinks:
    print(drinks[name])
else:
        print("Unbekannter Name")