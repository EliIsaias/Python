print ("Ejercicio 2 \n\t\tListas \n")
n = int(input("Ingresa el numero de asignaturas: "))
print ("Ingresa las asignaturas: ")
asignatura = []
for  i in range (n):
    asignatura.append(input())

print ("\nLas asignaturas ingresadas son: ")
for i in asignatura:
    print (i)
