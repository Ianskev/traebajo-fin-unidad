import os
import time
import csv

BOLD = '\033[1m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

def printOptions():
    print(BOLD + BLUE+"|--------------------------------------------------|")
    print("|-----------------MENU DE OPCIONES-----------------|")
    print("|--------------------------------------------------|\n"+ RESET)
    print(BOLD + RED +'[1]'+RESET +' Leer archivo .csv o .txt')
    print(BOLD + RED +'[2]'+ RESET + ' Listar libros ')
    print(BOLD + RED +'[3]'+ RESET +' Agregar Libros')
    print(BOLD + RED +'[4]'+ RESET +' Eliminar Libros')
    print(BOLD + RED +'[5]'+ RESET +' Buscar libros por ISBN o Titulo')
    print(BOLD + RED +'[6]'+ RESET +' Ordenar los libros por titulos')
    print(BOLD + RED +'[7]'+ RESET +' Buscar libros editorial,genero o autor')
    print(BOLD + RED +'[8]'+ RESET +' Buscar libro por número de autores')
    print(BOLD + RED +'[9]'+ RESET + ' Editar libro')
    print(BOLD + RED +'[10]'+ RESET +' Guardar libro en .csv o .txt')
    print(BOLD + RED +'[11]'+ RESET +' Salir'+RESET)
    print("-" * 20)

class Book:
    def __init__(self, id:str, title:str, genre:str, ISBN:str, editorial:str, autors:str):
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autors = autors
    def get_atributos(self):
        return self.__id,self.__title,self.__genre,self.__ISBN,self.__editorial,self.__autors

    def set_atributos(self, id,tittle,genre,ISBN,editorial,autors):
        self.__id = id
        self.__title = tittle
        self.__genre = genre
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autors = autors
        
def repeatOptions():
    dato = input("\n¿Desea volver al menu? (S: Sí - N: No):  ").lower()
    if dato == 's':
        run()
    else:
        os._exit(0)
def run():
    printOptions()
    command = input(BOLD+"Selecciona una opción: "+RESET)

    if command == '1':
        pass
    elif command == '2':
        pass
    elif command == '3':
        pass
    elif command == '4':
        pass
    elif command == '5':
        pass
    elif command == '6':
        pass
    elif command == '7':
        pass
    elif command == '8':
        pass
    elif command == '9':
        pass
    elif command == '10':
        pass
    elif command == '11':
        os._exit(1)
    else:
        print('Opcion inválida, ingrese un numero del 1 al 11')
        time.sleep(2)
        run()

if __name__ == "__main__":
    run()
