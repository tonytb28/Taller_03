"""
Modelo lo cual incluye todos los datos de
la conexion de base de datos y las clases """


class Ciudad:                              # creacion de la clase ciudad
    def __init__(self,identif,consumo):
        self.identif = identif
        self.consumo = consumo



class Subestacion:                                          # creacion de la clase subestacion
    def __init__(self,ciudad,consumo_total,identif,consumo):
        self.ciudad = ciudad
        self._consumo= Ciudad(identif,consumo)
        
            
class Operador:                                   # creacion de la clase ciudad
    def __init__(self,nombre,ID_operador):
        self.nombre = nombre
        self.ID_operador = ID_operador
        