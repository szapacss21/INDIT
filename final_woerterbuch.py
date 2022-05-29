wb = {"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}

print("Welcome to en2ger, please select the desired function")
print("Choose [T] to translate")
print("Choose [A] to add new word")
    

    
correct = False
    
while correct == False:       
    eing = input("Enter a function: ")    
    
    if eing == "T":
        word=input("Please enter your word: ") 
        if word in wb:
            print("translation: ",wb[word]) 
        else:
            print('not found')
    elif eing == "A":
        
        wb[input('English word:')] = input('German translation:') 
     
        
    else:
        print("Unknown answer")