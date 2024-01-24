print("*************************")
print("******BIENVENIDO(A)*******")
print("***A TENDA DE FILHOTES****")
print("*************************")

num_perros = 10
num_gatos = 8
num_pajaros = 25
animales_totales = num_perros + num_gatos + num_pajaros

print("Por favor, ingresa tu nombre:")
nombre = input()
print("Por favor, escribe tu apellido:")
apellido = input()

nombre_completo = nombre + " " + apellido
print("Gracias por visitarnos,", nombre_completo)

while True:
    print("")
    print("=================================")
    print("Selecciona la opción que deseas:")
    print("1: Conocer cuántos animales tiene la tienda.")
    print("2: Comprar un animal")
    print("3: Salir del programa")

    respuesta = int(input())

    if respuesta == 1:
        print("Actualmente contamos con")
        print("Perros:", num_perros, "Gatos:", num_gatos, "Pajaros:", num_pajaros)
        print("En total tenemos", animales_totales, "animales.")
    elif respuesta == 2:
        print("Qué animal deseas comprar?")
        animal = input()
        print("Has comprado un", animal)
    elif respuesta == 3:
        print("Saliendo del programa")
        break