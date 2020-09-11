from flask import Flask, jsonify,request,url_for,render_template
from Controller.Departamento_Controller import Departamento_Controller
from Controller.Producto_Controller import Producto_Controller
from Database.db import get_db

app = Flask(__name__)

@app.route('/')
def index():
    db = get_db()
    inicio = db.execute(
        'SELECT d.id, nombre, id_product'
        ' FROM departamentos d JOIN productos p ON d.id_product = p.id_product'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('index.html', inicio = inicio)

@app.route('/productos', methods=['GET', 'POST'])
def getProductos():
    try:
        controlador = Producto_Controller()
        respuesta = controlador.VerProductos(request)
        return respuesta   
    except Exception as ex:
        error = Error()
        return error.Render(str(ex))

@app.route('/productos/<string:id_product>',methods=['GET'])
def getProducto(id_product):
    producto = Producto_Controller.VerProducto(id_product)

    if producto==None:
        return jsonify({"Mensaje": "Producto no se encontró"})

    return jsonify({"Producto":producto})


@app.route('/productos/nuevo', methods=['GET', 'POST'])
def crear_Producto():
    try:
        producto =Producto_Controller()
        crear= producto.crearProducto(request)
        return crear
    except Exception as ex:
        error= Error()
        return error.Render(str(ex))


@app.route('/productos/actualizar', methods=['GET', 'POST'])
def Actualizar_producto():
    try:
        producto = Producto_Controller()
        actualizar = producto.ActualizarProducto(request)
        return actualizar
    except Exception as ex:
        error = Error()
        return error.Render(str(ex))


@app.route('/productos/eliminar', methods=['GET', 'POST'])
def Eliminar_producto():
    try:
        producto  = Producto_Controller()
        eliminar = producto.EliminarProducto(request)
        return eliminar
    except Exception as ex:
        error = Error()
        return error.Render(str(ex))


@app.route('/departamentos/crear', methods=['GET', 'POST'])
def crearDepartamento():
    try:
        departamento = Departamento_Controller()
        crearDep = departamento.CrearDepartamento(request)
        return crearDep
    except Exception as ex:
        error = Error()
        return error.Render(str(ex))


@app.route('/departamentos/<string:id>', methods=['GET'])
def verDepartamento(id):
    try:
        departamento = Departamento_Controller()
        verDep = departamento.VerDepartamento(id)

        if departamento ==None:
            return jsonify({"mensaje": "Departamento no encontrado"})

        return jsonify({"Departamento": departamento})

@app.route('/departamentos', methods=['GET', 'POST'])
def getDepartamentos():
    try:
        controlador = Departamento_Controller()
        resp = controlador.VerDepartamentos(request)
        return resp
    except Exception as ex:
        error = Error()
        return error.Render(str(ex))


class Error:

    def Render(self, mensaje):
        print(mensaje)
        return "Ha ocurrido un error: " + mensaje



