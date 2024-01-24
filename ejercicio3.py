v1 = float(input("Ingrese el voltaje 1: \n"))
v2 = float(input("Ingrese el voltaje 2: \n"))
v3 = float(input("Ingrese el voltaje 3: \n"))

prom = (v1 + v2 + v3) / 3

if prom <= 115:
    print ("VOLTAJE CORRECTO ")
elif prom > 115 and prom <= 220:
    print ("ALTO VOLTAJE")
elif prom > 220:
    print ("PELIGRO")
