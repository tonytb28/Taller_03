from Model.Producto_Model import Producto_Model

class Producto_Controller:
    def VerProducto(self, request):
        parametros = self.ObtenerParametros(request)
        modelo = Producto_Model()
        producto = modelo.VerProducto(parametros)

        return producto

    def VerProductos(self, request):
        modelo =Producto_Model()
        producto = modelo.VerProductos()
        return producto


    def crearProducto(self, request):
        parametros= self.ObtenerParametrosCrear(request)
        modelo = Producto_Model()
        nuevoProducto = modelo.NuevoProducto(parametros)
        return nuevoProducto


    def EliminarProducto(self, request):
        parametros = self.ObtenerParametros(request)
        modelo= Producto_Model()
        respuesta = modelo.EliminarProducto(parametros)
        return respuesta


    def ActualizarProducto(self, request):
        parametros =self.ObtenerParametrosActualizar(request)
        modelo= Producto_Model()
        respuesta= modelo.ActualizarProducto(parametros)
        return respuesta

    def ValidarParametrosCrear(self, parametros):
        return True


    def ObtenerParametrosCrear(self, request):
        parametros = {
            "id_product": request.form['id_product'],
            "descripcion": request.form['descripcion'],
            "precio": request.form['precio']
        }
        if self.ValidarParametrosCrear(parametros):
            return parametros
        else:
            return parametros

        raise Exception("Error de parametros")

    
    def ObtenerParametros(self, request):
        parametros = {
            "id_product": request.form['id_product']
        }
        return parametros

    def ObtenerParametrosActualizar(self, request):
        parametros = {
            "id_product": request.form['id_product'],
            "descripcion": request.form['descripcion'],
            "precio": request.form['precio']
        }
        return parametros