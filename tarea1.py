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

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_genre(self):
        return self.__genre
    def get_ISBN(self):
        return self.__ISBN
    def get_editorial(self):
        return self.__editorial
    def get_autors(self):
        return self.__autors

def repeatOptions():
    dato = input("\n¿Desea volver al menu? (S: Sí - N: No):  ").lower()
    if dato == 's':
        run()
    else:
        os._exit(0)

def listBooks():
    print('----------------------------------------------------------------------------------------------------------------------------------------')
    print('|                                                                 Lista de libros                                                      |')
    print('----------------------------------------------------------------------------------------------------------------------------------------')
    print(f'|  ID  | Titulo                                  | Genero    | ISBN                | Editorial                | autor(es)              |')
    print('----------------------------------------------------------------------------------------------------------------------------------------')
    
    with open("Registros Libros.csv",'r') as file:
        reader = csv.reader(file)
        next(reader)

        for id, title,genre,isbn,editorial,autor in reader:
            print(f"| {id:5}| {title:40}| {genre:10}| {isbn:20}| {editorial:25}| {autor:23}|")

    print('----------------------------------------------------------------------------------------------------------------------------------------')
    repeatOptions()

def addNewBook():
    with open("Registros Libros.csv",'a',newline='\n') as file:
        print('CREAR REGISTRO DE LIBRO')
        print('*' * 50)
        Id = input("\nID: ").upper()
        title = input("Title: ").capitalize()
        genre = input("Genre: ").capitalize()
        isbn = input("ISBN: ")
        editorial = input("Editorial: ").title()
        author = input("Author(s): ").title()
        add_list = [Id, title, genre, isbn, editorial, author]
        
        add = csv.writer(file) 
        add.writerow(add_list) 
        file.close()

    print("Se agregó el libro de forma correcta.")
    repeatOptions()

def showHeader():
    print('----------------------------------------------------------------------------------------------------------------------------------------')
    print('|                                                                 Resultado                                                             |')
    print('----------------------------------------------------------------------------------------------------------------------------------------')
    print(f'|  ID  | Titulo                                  | Genero    | ISBN                | Editorial                | autor(es)              |')
    print('----------------------------------------------------------------------------------------------------------------------------------------')

#Opcion5
def searchByIsbnOrTitle():
    print("1) ISBN\n2) Titulo")
    opcion = input("Elige una opcion:  ")

    if opcion == '1':
        isbnx = input('Ingresar el ISBN del libro: ')
        with open("Registros Libros.csv",'r') as file:
            reader = csv.reader(file)
            data=[line for line in reader]
            for row in data:
                if row[3]==isbnx:
                    show_data = []
                    show_data.append(row)
                    showHeader()
                    #print(show_data[0])
                    print(f"| {show_data[0][0]:5}| {show_data[0][1]:40}| {show_data[0][2]:10}| {show_data[0][3]:20}| {show_data[0][4]:25}| {show_data[0][5]:23}|")
                    show_data.clear()
                    repeatOptions()
        print("\nEl ISBN es incorrecto o no existe")
        repeatOptions()

               
    elif opcion == '2':
        titulox=input('Ingresar el Titulo del libro: ')
        with open("Registros Libros.csv",'r') as file:
            reader = csv.reader(file)
            data=[line for line in reader]
            for row in data:
                if row[1]==titulox:
                    show_data = []
                    show_data.append(row)
                    showHeader()
                    #print(show_data[0])
                    print(f"| {show_data[0][0]:5}| {show_data[0][1]:40}| {show_data[0][2]:10}| {show_data[0][3]:20}| {show_data[0][4]:25}| {show_data[0][5]:23}|")
                    show_data.clear()
                    repeatOptions()
        print("\nEl ISBN es incorrecto o no existe")
        repeatOptions()


def updateBook():
    id2 = input('Ingrese el ID del libro a actualizar: ')
    with open("Registros Libros.csv", 'r') as file:
        reader = csv.reader(file)
        data = [line for line in reader]
        for row in data:
            if row[0] == id2:
                data.remove(row)
        title = input('Ingrese el titulo del libro: ').title()
        genre = input('Insertar el genero del libro: ').title()
        ISBN = input('Ingrese el código ISBN: ').title()
        editorial = input('Ingrese el editorial: ').title()
        autores = input('Ingrese el autor(es): ').title()
        libronuevo = []

        libro = Book(id2, title, genre, ISBN, editorial, autores)

        libronuevo.append(libro.get_id())
        libronuevo.append(libro.get_title())
        libronuevo.append(libro.get_genre())
        libronuevo.append(libro.get_ISBN())
        libronuevo.append(libro.get_editorial())
        libronuevo.append(libro.get_autors())
        data.append(libronuevo)
        data.sort()

    with open("Registros Libros.csv", 'w', newline='') as file:
        w = csv.writer(file)
        w.writerows(data)

        # print(data)
        # next(reader)4

    print("Se ha modificado el libro de ID " + id2 + " correctamente")

    repeatOptions()


def SaveBooks():
    with open("Registros Libros.csv", 'r') as file:
        reader = csv.reader(file)
        data = [line for line in reader]
        namefile = input('Ingrese el nombre del archivo a guardar (ejemplo: libros.txt o libros.csv''): ')
    with open(namefile, 'w') as f:
        f.write("ID, Título, Género, ISBN, Editorial, Autor(es)\n")
        for list in data:
            f.write("\n")
            f.write(','.join(list))

    repeatOptions()

def run():
    printOptions()
    command = input(BOLD+"Selecciona una opción: "+RESET)

    if command == '1':
        print("¿ QUE DESEA REALIZAR ?")
        pedido=int(input("ESCRIBE 1 SI DESEA CARGAR ARCHIVO CSV "))            
        if pedido==1:
            f = open("Registros Libros.csv", "r")
            line= 4
            for x in range(line):
                a = f.readline()
                print(a)                                                          
        else:
            print("INGRESE UNA OPCION VALIDA")  
        repeatOptions()  
    elif command == '2':
        listBooks()
    elif command == '3':
        addNewBook()
    elif command == '4':
        try:
            with open("Registros Libros.csv") as file:
                newFile = csv.reader(file)
                data = [i for i in newFile]

            with open("Registros Libros.csv", "w", newline='') as file:
                Id = input(BOLD + "\nIngrese el ID del libro que desea eliminar: " + RESET)
                new = csv.writer(file)
                for r in data:
                    for c in r:
                        if c != Id:
                            new.writerow(r)
                        break
                file.close()
        except:
            print("\nNo Hay datos en el csv.")
        else:
            print("\nEliminado correctamente.")
            repeatOptions()

    elif command == '5':
        searchByIsbnOrTitle()
    elif command == '6':
        pass
    elif command == '7':
        pass
    elif command == '8':
        pass
    elif command == '9':
        updateBook()
    elif command == '10':
        SaveBooks()
    elif command == '11':
        os._exit(1)
    else:
        print('Opcion inválida, ingrese un numero del 1 al 11')
        time.sleep(2)
        run()

if __name__ == "__main__":
    run()