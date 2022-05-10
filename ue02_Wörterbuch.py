woerterbuch = {"apfel":"apple","birne":"pear","kirsche":"cherry","melone":"melon","marille":"apricot","pfirsich":"peach"}   #erstellung Wörterbuch als dict


eingabe = input("Eingabe des deutschen Wortes:  ")  
eingabe = eingabe.lower()    

if eingabe not in woerterbuch:  
    print("Wort nicht gefunden") #ausgabe
    
else:
    print("Übersetzung Englisch:   ", woerterbuch[eingabe]) 