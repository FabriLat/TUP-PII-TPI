# Crear un diccionario para cada libro
import random, string, os
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def generar_codigo():
    #completar
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod

def nuevo_libro():
    #completar
    titulo = str(input("Ingrese el titulo del libro: "))
    autor = str(input("Ingrese el autor del libro: "))
    cant_ej_ad = int(input("Ingrese la cantidad de libros adquiridos: "))
    cant_ej_pr = int(0)
    cod = generar_codigo()
    nuevo_libro = {
        "cod": cod,
        "cant_ej_ad": cant_ej_ad,
        "cant_ej_pr": cant_ej_pr,
        "autor": autor,
        "titulo": titulo
    }
    os.system("cls")

    print("Libro registrado con éxito.\n")
    print("Titulo:",nuevo_libro["titulo"])
    print("Autor:",nuevo_libro["autor"])
    print("Cantidad adquirida:",nuevo_libro["cant_ej_ad"])
    print("Codigo:",nuevo_libro["cod"])
    return nuevo_libro

  