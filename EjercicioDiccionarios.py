print ("Ejercicio 3 \n\t\tDiccionarios \n")

d = {"Brocolí" : "8.55", "Pepino" : "6.87", "Calabaza" : "11.55", "Chayote" : "14.33"}

print ("La lista de verduras es: ")
print (d)

verdura = input("\nElija su verdura: ")
k = float(input("Elija los kilos que desee: "))

precio =float(d[verdura]) 
valorf =precio * k

print ("El precio final de",verdura, "es: ", valorf)
