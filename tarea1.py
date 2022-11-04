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

lista_de_libros = []
def leer_archivos(nombre_archivo):
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        rows = csv.DictReader(f)
        for r in rows:
            lista_de_libros.append(r)
def lista_libr():
    for elem in lista_de_libros:
        for k,v in elem.items():
            print(k, v)
leer_archivos("tarea_final.txt")
lista_libr()
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
