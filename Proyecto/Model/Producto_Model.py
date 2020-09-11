
from Database.db import get_db

class Producto_Model:
    def VerProductos(self):
        db = get_db()
        productos =db.execute(
            'SELECT * FROM productos'
        ).fetchall()
        return productos


    def VerProducto(self, parametros):
        db=get_db()
        producto = db.execute(
            'SELECT * FROM productos WHERE id_product = ?',(parametros.get("id_product"))
        ).fetchall()
        return producto


    def NuevoProducto(self,parametros):
        db = get_db()
        db.execute(
            'INSERT INTO productos (id_product, descripcion,precio)'
            ' VALUES (?,?,?)',
            (parametros.get("id_product"),parametros.get("descripcion"),parametros.get("precio"))
        )
        db.commit()


    def ActualizarProducto(self,parametros):
        db = get_db()
        db.execute(
            'UPDATE productos SET descripcion = ?, precio = ?'
            ' WHERE id_product = ?',
            (parametros.get("descripcion"), parametros.get("precio"), parametros.get("id_product"))
        )
        db.commit()
        producto = db.execute(
            'SELECT * FROM productos WHERE id_product = ?', (parametros.get("id_product"))
        ).fetchall()
        return producto


    def EliminarProducto(self,parametros):
        db = get_db()
        db.execute(
            'DELETE FROM productos WHERE id_product = ?', (parametros.get("id_product"))
        )
        db.commit()
        return 'Mensaje eliminado.'
