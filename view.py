class ViewOperador:
    def __init__(self,Operador):
        self.datos_operador = Operador

    def datos_operador(self):
        print("Operador: "+repr(self.datos_operador))


class View_Subestacion:
    def __init__(self,Subestacion):
        self.datos_Subestacion  = Subestacion

    def datos_Subestacion(self):
        self.Ciudad = View_Ciudad


class View_Ciudad:
    def __init__(self,Ciudad):
        self.datos_Ciudad = Ciudad