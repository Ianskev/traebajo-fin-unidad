import requests
import csv
class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial, autor):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor

    def get_atributos(self):
        return self.__id, self.__titulo, self.__genero, self.__isbn, self.__editorial, self.__autor

    def set_atributos(self,id, titulo, genero, isbn, editorial, autor):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor
    
    def __del__(self):
        return None
    
    #Opcion 3
    def agregar_libro(self):
        with open(file_name+".csv", 'a', newline='\n') as file:
            def ingresar_libro():
                estructura = ['id', 'titulo','genero', 'editorial', 'autor']
                for iterador in estructura:
                    iterador = input(f'Ingrese {iterador}: ')
                    add_list.append(iterador)
                
                add.writerow(add_list)
ingresar_libro()


def obtener_csv_como_lista_de_diccionarios(nombre_archivo):
    separador = ","
    with open(nombre_archivo, encoding="utf-8") as archivo:
        dic = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            columnas = linea.split(separador)
            id = columnas[0]
            titulo = columnas[1]
            genero = columnas[2]
            isbn = columnas[3]
            editorial = columnas[4]
            autor = columnas[5]
            dic.append({
            "id": id,
            "titulo": titulo,
            "genero": genero,
            "isbn": isbn,
            "editorial": editorial,
            "autor":autor})
        return dic

def main():
    print("Bienvenidos")
    print("Opcion 3")

main()
print(obtener_csv_como_lista_de_diccionarios("tarea_final.txt"))
