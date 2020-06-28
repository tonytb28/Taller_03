import sqlite3
from sqlite3 import Error
from model import Operador


def sqlite_create_database():
    try:
        conn = sqlite3.connect('taller_03.db')
        
    except Error as er:
        print(er)
        
    

def create_table(conn):
    try:
        _Cursor = conn.cursor()
        _Cursor.execute("CREATE TABLE operador(ID_operador INTEGER KEY AUTOINCREMENT, nombre text ")
        conn.commit()
    except Error:
        print(Error, "No se creo la tabla")
    
    def insert_new (nombre):
        try:
            _Cursor = conn.cursor()
            _Cursor.execute("INSERT INTO operador(nombre) VALUE(?)",nombre)
            conn.commit()
        except Error:
            print(Error,"Error en los valores ingresados")

    insert_new(Operador.nombre)


