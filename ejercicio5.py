# cada carácter deberá ser encriptado a ocho caracteres;
#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.


class Encriptar:
    def __init__(self, texto):
        self.texto=texto
        self.tabla_encriptar={}
        self.tabla_desencriptar={}
        self.encriptado=""
        self.desencriptado=""
        self.generar_tablas()