# cada carácter deberá ser encriptado a ocho caracteres;
#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Encriptador:
    def __init__(self, texto):
        self.texto=texto
        self.encriptado=""
        self.desencriptado=""
        self.encriptar()
        self.desencriptar()

    def encriptar(self):
        for i in self.texto:
            self.encriptado+=chr(ord(i)+8)

    def desencriptar(self):
        for i in self.encriptado:
            self.desencriptado+=chr(ord(i)-8)

    def __str__(self):
        return "Texto encriptado: "+self.encriptado+". Texto desencriptado: "+self.desencriptado+"."

def Encriptar(texto):
    encriptador=Encriptador(texto)
    return encriptador


texto=Encriptar("el desarrollo de un algoritmo de encriptacion para las comunicaciones rebeldes")
print(texto)

