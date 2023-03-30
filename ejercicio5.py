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

