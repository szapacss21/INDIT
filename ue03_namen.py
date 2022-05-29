namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]


 
 def begruessung(name):
     print("Hallo ",name)
     return
     
     
def begruessung2 (namenliste):
    for ein_name in namenliste:
        print("Hallo", ein_name)
        return
        
        
print("Version ")
for name in namen:
       begruessung(name)
       
print("Version 1")
begruessung2(name)
