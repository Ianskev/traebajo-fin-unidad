class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial, autor):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor #autores

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
    
    #1
    def leer_libro(self):
        libro = open(f'database/{id}.txt','r')
        libro = libro.readlines()

libro = Libro(12345,"El caminante y su sombra","Drama", 12345678,"Laeditoral","Alberth Camus")
libro.leer_libro()