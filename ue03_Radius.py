import math

def eingabe():
    input()
    coreect = False
    
    while correct == False:
        r_str = input("Eingabe radius")
        
        try:
            r = float(r_str)
            if r > 0:
                correct = True
            else:
                print("keine gültige Eingabe (r <= 0)")
            
        except VaureError:
            print("Keine gültige Zahl")
            return r
        
        def kreisumfang(radius):
            umfang = 2*radius*math.pi
            return umfang
        
    
    return radius_eingeben

kreisradius = eingabe()
print("eingegebener Radius: ", kreisradius)

umfang = kreisumfang(kreisradius)
print("Kreisumfang: ",umfang)