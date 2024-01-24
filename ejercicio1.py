v1 = float(input("Ingrese el voltaje 1: "))
v2 = float(input("Ingrese el voltaje 2: "))
v3 = float(input("Ingrese el voltaje 3: "))
v4 = float(input("Ingrese el voltaje 4: "))
v5 = float(input("Ingrese el voltaje 5: "))

prom = (v1 + v2 + v3 + v4 + v5) / 5

if prom > 220:
    print ("ALTO VOLTAJE ")
elif prom <= 220:
    print ("VOLTAJE CORRECTO")