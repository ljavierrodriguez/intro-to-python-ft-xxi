""" OOP (Object Oriented Programming) """

class Figura:
    def __init__(self):
        print("Instanciando la clase Figura")
        self.area = 0
        
    def calcular_area(self):
        pass
    
    def getArea(self):
        return self.area
        
"""         
fig = Figura()
fig.calcular_area()
fig.getArea()
"""

class Cuadrado(Figura):
    def __init__(self):
        super().__init__()
        self.lado = 0
        
    def calcular_area(self, lado):
        self.area = lado * lado
        

cuadrado = Cuadrado()
cuadrado.calcular_area(10)
print(cuadrado.getArea())


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        self.area = (self.base * self.altura) / 2
        
        
triangulo = Triangulo(20, 14)
triangulo.calcular_area()
print(triangulo.getArea())


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def mostrar_informacion(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}"
    
lib1 = Libro("El Gran Gatsby", "Fitzgerald");
lib2 = Libro("100 Años de Soledad", "Gabriel Garcia Marquez");
lib3 = Libro("Harry Potter", "J.K Rowling");


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def mostrar_catalogo_libros(self):
        if len(self.libros) > 0:
            for libro in self.libros:
                print(libro.mostrar_informacion())
        else:
            print("Sin disponibilidad de Libros")
            
            
biblioteca = Biblioteca("Biblioteca Nacional de Chile")
biblioteca.mostrar_catalogo_libros()
biblioteca.agregar_libro(lib1)
biblioteca.agregar_libro(lib2)
biblioteca.agregar_libro(lib3)
biblioteca.mostrar_catalogo_libros()