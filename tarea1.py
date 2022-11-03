from csv import *
import os
import time


class Libro:
    def __init__(self, id: int, titulo:str, genero:str, isbn:int, editorial:str, autor:str) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor
    
    def get_atributos(self):
        return self.__id, self.__titulo, self.__genero, self.__isbn, self.__editorial, self.__autor
    
    def set_atributos(self, id, titulo, genero, isbn, editorial, autor):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor

    def __del__(self):
        return None

    #Opcion 3
    def agregar_libro(self,id, titulo, genero, isbn, editorial, autor):
        dict = [id,titulo,genero,isbn,editorial,autor]
        with open("database.csv",'a') as database:
            add = writer(database)
            add.writerow(dict)


def clean():
    os.system("cls" if os.name =="nt" else "clear")

def timer(n):
    time.sleep(n)

def opcion_3(): 
    estructura = ['id','titulo','genero','isbn', 'editorial','autor']
    dict_to_add = []
    for iterador in estructura:
        tmp = input(f'Ingrese {iterador}:')
        dict_to_add.append(tmp)
    return dict_to_add


def menu():
    print("="*52)
    print("Bienvenido a la Biblioteca de Alexandria de Silabuz")
    print("="*52)
    print("Ingrese el numero de la opcion que desea realizar:")
    opciones = ['Leer archivo de disco duro', 'Listar Libros',
                'Agregar Libro', 'Eliminar Libro', 'Buscar Libro por ISBN o por titulo',
                'Ordenar libros por titulo','Buscar Libros por Autor, editorial o genero',
                'Buscar Libros por numero de autores','Editar o actualizar libro','Guardar Libro','Salir']
    for i in range (len(opciones)):
        print(f'{i+1}: {opciones[i]}')
    print('-'*52)

    opcion_usuario = int(input("?:"))
    if(opcion_usuario == 3):
        print(f"Selecciono' la opcion {opciones[opcion_usuario -1]}:")
        usuario_input = tuple(opcion_3())
        libro = Libro(*usuario_input)
        parametros = libro.get_atributos()
        libro.agregar_libro(*parametros)
        print("\nLibro agregado satisfactoriamente\n")
        timer(5)
        clean()
        #menu()



menu()
