3# Trabajo Práctico I - Programación II
import os
import bibloteca as b
print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar prestamo")
    print("2 - Gestionar devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantallaCRBJsAkS
    if opt.isnumeric():
        if int(opt) == 1:
            b.prestar_ejemplar_libro()
        elif int(opt) == 2:
            b.devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            b.registrar_nuevo_libro()
            #completar
            print()
        elif int(opt) == 4:
            #completar
            b.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            b.ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        elif (int(opt) < 1 or int(opt) > 6): 
            print("Error, la opción elegida está fuera del rango 1-6")
    else: 
        print("Ingrese una opción numérica que esté dentro del rango 1-6")
    input("Presione cualquier tecla para continuar....") # Pausa
    os.system ("cls") #Limpiar pantalla

print("Hasta luego!.")