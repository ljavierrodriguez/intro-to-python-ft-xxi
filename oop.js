/* OOP (Object Oriented Programming) */

class Figura {
    constructor(){
        console.log("Instanciando la clase Figura")
        this.area = 0;
    }

    calcularArea(){}

    getArea(){
        return this.area;
    }
}
/* 
let fig = new Figura();
fig.calcularArea()
fig.getArea() 
*/

class Cuadrado extends Figura {
    constructor(){
        super();
        this.lado = 0;
    }

    calcularArea(lado){
        this.area = lado*lado;
    }
}

let cuadrado = new Cuadrado();
cuadrado.calcularArea(10)
console.log(cuadrado.getArea())

class Triangulo extends Figura {
    constructor(base, altura){
        super();
        this.base = base;
        this.altura = altura;
    }

    calcularArea(){
        this.area = (this.base * this.altura) / 2;
    }
}

let triangulo = new Triangulo(10, 15);
triangulo.calcularArea();
console.log(triangulo.getArea())


class Libro {
    constructor(titulo, autor){
        this.titulo = titulo;
        this.autor = autor;
    }

    mostrarInformacion(){
        return `Titulo: ${this.titulo}\nAutor: ${this.autor}`;
    }
}

let lib1 = new Libro("El Gran Gatsby", "Fitzgerald");
let lib2 = new Libro("100 Años de Soledad", "Gabriel Garcia Marquez");
let lib3 = new Libro("Harry Potter", "J.K Rowling");
//console.log(lib1.mostrarInformacion())


class Biblioteca {
    constructor(nombre){
        this.nombre = nombre;
        this.libros = [];
    }

    agregarLibro(libro){
        this.libros.push(libro)
    }

    mostrarCatalogoLibros(){
        if(this.libros.length > 0){
            this.libros.forEach((libro) => {
                console.log(libro.mostrarInformacion())
            })
        } else {
            console.log("Sin disponibilidad de Libros")
        }
    }
}

let biblioteca = new Biblioteca("Biblioteca Nacional de Chile");
biblioteca.mostrarCatalogoLibros()
biblioteca.agregarLibro(lib1)
biblioteca.agregarLibro(lib2)
biblioteca.agregarLibro(lib3)
biblioteca.mostrarCatalogoLibros()
