import csv
from model import Operador, Ciudad, Subestacion
from view import ViewOperador,View_Ciudad,View_Subestacion

# importamos las clases desde model y view con sus respectivos datos.

##################Operador####################
class Controller_Operador():
    def __init__(self):
        self.obj_Operador = self.getDatosOperador()
        self.vista_operador = ViewOperador(self.obj_Operador)
    
    def getDatosOperador(self,nombre):
        operador = Operador(nombre)
        return operador

    def callView_Operador(self):
        self.vista_operador.datos_operador()

#################Clase para obtener datos desde el archivo .csv###############
class obtener_Datos(indice):
    def generar_Ciudades(self,indice):
        output = []

        ReadFile = open('C:\Desarollo\Python\mediciones.csv')
        for line in ReadFile:
            cells = line.split(';')
            output.append((cells[indice]))
            lis_sinDuplicados = list(dict.fromkeys(output))
        ordenar_list=sorted(lis_sinDuplicados,key=int)
        ReadFile.close

    def Datos(self,Ind):
        output = []
        ReadFile = open('C:\Desarollo\Python\mediciones.csv')
        for line in ReadFile:
            cells = line.split(';')
            output.append((cells[Ind]))
        ReadFile.close

    def Maximo (self,listados):
        max_item= max(listados, key=int)
        

##############Subastacion#######################
class Controller_Subestacion:
    def __init__(self):
        self.readFile = self.getMediciones()
        self.Generar_Subestacion = generar_Ciudades(self.readFile)
        self.readFile = self.getHora()


    def getMediciones(self):
        with open('C:\Desarollo\Python\mediciones.csv') as csvarchivo:
            entrada = csv.reader(csvarchivo)                

    def generar_Ciudades(self):
        obtener_Datos.generar_Ciudades(1)
        
    

    def getHora(self):
        obtener_Datos.Datos(0)
        obtener_Datos.Maximo(obtener_Datos.Datos)
        



###################Ciudad############################
class Controller_Ciudad:
    def __init__(self):
        self.obj_Ciudad = self.getConsumo()
        self.getConsumo = self.Calcular_Consumo()

    def getConsumo(self):
        obtener_Datos.Datos(2)
