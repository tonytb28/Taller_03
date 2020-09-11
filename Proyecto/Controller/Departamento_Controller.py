from Model.Departamento_Model import Departamento_Model

class Departamento_Controller:
    def VerDepartamentos(self, request):
        modelo = Departamento_Model()
        departamentos = modelo.VerDepartamento()
        return departamentos

    def VerDepartamento(self, request):
        modelo = Departamento_Model()
        departamento = modelo.VerDepartamento(self.ObtenerParametros)
        return departamento

    def CrearDepartamento(self, request):
        parametros= self.ObtenerParametrosCrear(request)
        dep = Departamento_Model()
        nuevoDepartamento = dep.CrearDepartamento(parametros)
        return nuevoDepartamento

    def ObtenerParametros(self, request):
        parametros = {
            "id":request.form['id']
        }
        return parametros



    def ObtenerParametrosCrear(self, request):
        parametros = {
            "id": request.form['id'],
            "nombre": request.form['nombre'],
            "id_product": request.form['id_product']
        }
        if self.ValidarParametrosCrear(parametros):
            return parametros
        else:
            return parametros

        raise Exception("Error de parametros")
