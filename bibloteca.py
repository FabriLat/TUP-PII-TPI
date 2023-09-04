import libro as l
import os

# Crear una lista vacía para almacenar los libros
libros = []


# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
cant = len(libros)
print(cant)
def ejemplares_prestados():
#completar
        prestados = False
        for i in range(len(libros)):
            if libros[i]["cant_ej_pr"]  > 0:
                prestados = True
                print(f"Libro {i+1}: ")
                print(f"Titulo: ",libros[i]["titulo"])
                print(f"Autor: ",libros[i]["autor"])
                print(f"Cantidad prestados: {libros[i]['cant_ej_pr']}")
                print("==============================================")
        if prestados == False:
            return print("No hay libros prestados.")

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    #completar
    encontrado = False
    codigo = input("Ingrese el código del libro: ")
    for i in range(len(libros)):
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


def devolver_ejemplar_libro():
    #completar
    encontrado = False
    codigo = input("Ingrese el código del libro: ")
    for i in range(len(libros)):
        if libros[i]["cod"] == codigo:
            encontrado = True
            if libros[i]["cant_ej_pr"] > 0:  
                print(f"cantidad de libros prestados: {libros[i]['cant_ej_pr']}")
                libros[i]["cant_ej_ad"] = libros[i]["cant_ej_ad"] + 1
                libros[i]["cant_ej_pr"] = libros[i]["cant_ej_pr"] - 1
                input("Pulse 'ENTER' para realizar la devolución...")
                os.system ("cls")
                print("Devolución realizada con éxito.")
                return print(f"cantidad actualizada de libros prestados: {libros[i]['cant_ej_pr']}")   
            else:
                return print("Este libro no tiene ejemplares prestados.")

def nuevo_libro():
    #completar
    return None