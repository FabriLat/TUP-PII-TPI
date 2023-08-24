# Trabajo Práctico I - Programación II
import os
import bibloteca as b
import libro as l

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            #completar
            encontrado = False
            codigo = input("Ingrese el código del libro: ")
            for i in range(l.cant):
                if b.libros[i]["cod"] == codigo:
                    encontrado = True
                    print(f"Autor: ",b.libros[i]["autor"])
                    print(f"Titulo: ",b.libros[i]["titulo"])
                    print(f"Disponibles: ",b.libros[i]["cant_ej_ad"])
            if encontrado == False:
                print("Codigo erroneo.")




            print()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            #completar
            print()
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        elif (int(opt) < 1 or int(opt) > 6): 
            print("Error, la opción elegida está fuera del rango 1-6")
    else: 
        print("Ingrese una opción numérica que esté dentro del rango 1-6")
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")