libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]

import pprint
import time , os
from tabulate import tabulate

def visualizar_biblioteca():
    # return pprint.pprint(libros)
    encabezados = ["Titulo", "Autor", "Alquilado"]
    filas = [[libro["Titulo"], libro["Autor"], libro["Alquilado"]] for libro in libros]
    print(tabulate(filas, headers=encabezados, tablefmt="fancy_grid"))

def buscar_libro():
    pregunta = input("Que libro deseas buscar? ")
    for x in libros:
        if pregunta in x["Titulo"]:
            print(f"El libro '{pregunta}' si esta en la biblioteca")
            print(x)
            break
        else:
            print(f"El libro '{pregunta}' no esta en la biblioteca")
            break

def añadir_libro():
    pregunta_titulo = input("Que libro deseas añadir? ")

    if pregunta_titulo in libros["Titulo"]:
        print(f"El libro {pregunta_titulo} ya está en la biblioteca.")
        opcion = input("Desea añadir otro libro?(si/no): ")

        while opcion.lower() not in ["si", "no"]:
            print("Por favor, responde con 'si' o 'no'.")
            opcion = input("¿Desea añadir otro libro? (si/no): ")

        if opcion.lower() == "no":
            print("Opereacion cancelada")
            return
        
        elif opcion.lower() == "si":
            añadir_libro()
            return
        
    pregunta_autor = input("¿Quién es el autor del libro? ")        
    nuevo_libro = {"Titulo": pregunta_titulo, "Autor": pregunta_autor, "Alquilado": False}
    libros.append(nuevo_libro)

    print(f"El libro '{pregunta_titulo}' de {pregunta_autor} ha sido añadido a la biblioteca.")

def eliminar_libro():
    pregunta = input("Que libro deseas eliminar? ")
    for x in libros:
        if pregunta in x["Titulo"]:
            print(f"El libro {pregunta} eliminado con exito")
            libros.remove(x)

def alquilar_libro():
    pregunta = input("Deseas alquilar algun libro? ")
    if pregunta.lower() == "si":
        libro_alquilar = input("Qué libro quieres alquilar? ")
        encontrado = False
        for x in libros:
            if libro_alquilar == x["Titulo"]:
                encontrado = True
                if x["Alquilado"] == False:
                    x["Alquilado"] = True
                    print(f"Libro {libro_alquilar} ha sido alquilado con exito")
                else:
                    print(f"Libro {libro_alquilar} ya está alquilado")
                break

            elif not encontrado:
                print(f"El libro {libro_alquilar} no se encuentra en la biblioteca")

    elif pregunta.lower() == "no":
        print("Operacion cancelada")
    
    else:
        print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")

def devolver_libro():
    pregunta = input("Deseas devolver algun libro? ")
    if pregunta.lower() == "si":
        libro_devolver = input("Qué libro quieres devolver? ")
        encontrado = True
        for x in libros:
            if libro_devolver == x["Titulo"]:
                encontrado = False
                if x["Alquilado"] == True:
                    x["Alquilado"] = False
                    print(f"Libro {libro_devolver} ha sido devuelto con exito")
                else:
                    print(f"Libro {libro_devolver} ya está alquilado")
                break

            elif not encontrado:
                print(f"El libro {libro_devolver} no se encuentra en la biblioteca")

    elif pregunta.lower() == "no":
        print("Operacion cancelada")
    
    else:
        print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")


def mostrar_menu():
    while True:
        print("\n¿Qué desea hacer?")
        print("Pulse 1 para visualizar la biblioteca")
        print("Pulse 2 para buscar libro")
        print("Pulse 3 para añadir libro")
        print("Pulse 4 para eliminar libro")     
        print("Pulse 5 para alquilar un libro")
        print("Pulse 6 para devolver un libro")
        print("Pulse 7 para salir")

        opcion = input("Elija una acción a realizar: ")

        if opcion == "1":
            visualizar_biblioteca()  
        elif opcion == "2":
            buscar_libro()  
        elif opcion == "3":
            añadir_libro()  
        elif opcion == "4":
            eliminar_libro()  
        elif opcion == "5":
            alquilar_libro()  
        elif opcion == "6":
            devolver_libro()  
        elif opcion == "7":
            print("Hasta luego")
            break
        else:
            print(f"'{opcion}' no es válido. Introduzca un número del 1 al 7.")

        time.sleep(5)
        os.system("cls")

mostrar_menu()