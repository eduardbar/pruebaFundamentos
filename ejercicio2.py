b = float(input("ingrese la base del triángulo\n"))
a = float(input("ingrese la altura del triángulo\n"))

area = (b*a)/2 

if area > 1000:
    print ("DATOS NO VÁLIDOS")
else:
    print("El área es ", area )