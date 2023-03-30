#implementar sobre el TDA polinomio de la clase anterior, los siguientes métodos:
#restar
#dividir
#eliminar un termino
#determinar si un termino existe

class datoPolinomio:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

class nodoPolinomio:
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class Polinomio:
    def __init__(self):
        self.termino_mayor = None
        self.grado= -1

    def agregar_termino(self, coeficiente, exponente):
        if self.termino_mayor is None:
            self.termino_mayor = nodoPolinomio(datoPolinomio(coeficiente, exponente))
            self.grado = exponente
        else:
            aux = self.termino_mayor
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nodoPolinomio(datoPolinomio(coeficiente, exponente))
            if exponente > self.grado:
                self.grado = exponente

    def mostrar(self):
        aux = self.termino_mayor
        while aux is not None:
            print(aux.dato.coeficiente, "x^", aux.dato.exponente, end=" ")
            aux = aux.siguiente
        print()

    def evaluar(self, x):
        if self.termino_mayor is None:
            print("El polinomio no tiene terminos")
        else:
            aux = self.termino_mayor
            resultado = 0
            while aux is not None:
                resultado += aux.dato.coeficiente * (x ** aux.dato.exponente)
                aux = aux.siguiente
            return resultado