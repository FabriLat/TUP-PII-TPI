import libro as l
import os

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro(libros):
    #completar
    encontrado = False
    codigo = input("Ingrese el código del libro: ")
    for i in range(l.cant):
        if libros[i]["cod"] == codigo:
            encontrado = True
            if libros[i]["cant_ej_ad"] > 0:
                print(f"Autor: ",libros[i]["autor"])
                print(f"Titulo: ",libros[i]["titulo"])
                print(f"Disponibles: ",libros[i]["cant_ej_ad"])
                libros[i]["cant_ej_ad"] = libros[i]["cant_ej_ad"] - 1
                libros[i]["cant_ej_pr"] = libros[i]["cant_ej_pr"] + 1
                input("Pulse 'ENTER' para realizar el prestamo...")
                os.system ("cls")
                return print("Prestamo realizado con éxito.")
            else:
                print(f"Autor: ",libros[i]["autor"])
                print(f"Titulo: ",libros[i]["titulo"])
                return print("No quedan libros disponibles con este código.")
    if encontrado == False:
        libros[i]["cant_ej_ad"]
        return print("Codigo erroneo")


def devolver_ejemplar_libro(libros):
    #completar
    encontrado = False
    codigo = input("Ingrese el código del libro: ")
    for i in range(l.cant):
        if libros[i]["cod"] == codigo:
            if libros[i]["cant_ej_pr"] > 0:  
                encontrado = True
                print(f"cantidad de libros prestados: {libros[i]['cant_ej_pr']}")
                libros[i]["cant_ej_ad"] = libros[i]["cant_ej_ad"] + 1
                libros[i]["cant_ej_pr"] = libros[i]["cant_ej_pr"] - 1
                input("Pulse 'ENTER' para realizar la devolución...")
                os.system ("cls")
                print(f"cantidad actualizada de libros prestados: {libros[i]['cant_ej_pr']}")
                return print("Devolución realizada con éxito.")
            else:
                return print("Este libro no tiene ejemplares prestados.")
        else:
            return print("Codigo erroneo.")


def nuevo_libro():
    #completar
    return None