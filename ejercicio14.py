opcion = ""

while opcion != "salir":
    opcion = input ("Escribe 'hola', 'adios' o 'salir': ")
    if opcion == "hola":
        print("¡Hola!, mucho gusto!")
    elif opcion != "salir":
        print ("Opcion no valida")