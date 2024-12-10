from flask import request, redirect, url_for, Blueprint

from models.producto_model import Producto
from views import producto_view

producto_bp = Blueprint('producto', __name__, url_prefix="/producto")

@producto_bp.route("/")
def index():
    # Recupera todos los registros de productos
    productos = Producto.get_all()
    return producto_view.list(productos)

@producto_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        
        producto = Producto(nombre, precio, descripcion)
        producto.save()
        return redirect(url_for('producto.index'))
    return producto_view.create()

@producto_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    producto = Producto.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        
        # Actualiza los datos del producto
        producto.update(nombre=nombre, precio=precio, descripcion=descripcion)
        return redirect(url_for('producto.index'))
    return producto_view.edit(producto)

@producto_bp.route("/delete/<int:id>")
def delete(id):
    producto = Producto.get_by_id(id)
    producto.delete()
    return redirect(url_for('producto.index'))
