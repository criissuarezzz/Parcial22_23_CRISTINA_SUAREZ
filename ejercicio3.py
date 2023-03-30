class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def __str__(self):
        print("Nombre: "+self.nombre+" Nota: "+str(self.nota)+". Alumno creado con éxito.")

    def calificacion(self):
        if self.nota>=5:
            print("El alumno", self.nombre, "ha aprobado con un", self.nota)
        else:
            print("El alumno", self.nombre, "ha suspendido con un", self.nota)
            