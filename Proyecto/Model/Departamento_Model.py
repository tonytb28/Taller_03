
from Database.db import get_db


class Departamento_Model:
    
    def VerDepartamentos(self):
        db = get_db()
        departamentos = db.execute(
            'SELECT * FROM departamentos'
        ).fetchall()
        return departamentos

    def VerDepartamento(self, parametros):
        db = get_db()
        departamento = db.execute(
            'SELECT * FROM departamentos WHERE id = ?', (parametros.get("id"))
        ).fetchall()
        return departamento


    def CrearDepartamento(self, paramentros):
        db = get_db()
        db.execute(
            'INSERT INTO departamentos (id,nombre,id_product)'
            'VALUES (?,?,?)',
            (paramentros.get("id"),paramentros.get("nombre"),paramentros.get("id_product"))
        )
        db.commit()
        