from flask import request, redirect, url_for, Blueprint

from models.responsable_model import Responsable
from views import responsable_view

responsable_bp = Blueprint('responsable', __name__, url_prefix="/responsable")

@responsable_bp.route("/")
def index():
    # Recupera todos los registros de responsables
    responsables = Responsable.get_all()
    return responsable_view.list(responsables)

@responsable_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        fecha_nacimiento = request.form['fecha_nacimiento']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']     
        correo = request.form['correo']    
        id_recepcionista = request.form['id_recepcionista']
        
        responsable = Responsable(nombre, ap_paterno, ap_materno, fecha_nacimiento, sexo, telefono, direccion, ciudad, correo, id_recepcionista)
        responsable.save()
        return redirect(url_for('responsable.index'))
    return responsable_view.create()

@responsable_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    responsable = Responsable.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        fecha_nacimiento = request.form['fecha_nacimiento']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        direccion =request.form['direccion']
        ciudad = request.form['ciudad']     
        correo = request.form['correo']    
        id_recepcionista = request.form['id_recepcionista']
        
        # Actualiza los datos del responsable
        responsable.update(nombre=nombre, ap_paterno=ap_paterno, ap_materno=ap_materno, fecha_nacimiento=fecha_nacimiento, sexo=sexo, telefono=telefono, direccion=direccion, ciudad=ciudad, correo=correo, id_recepcionista=id_recepcionista)
        return redirect(url_for('responsable.index'))
    return responsable_view.edit(responsable)

@responsable_bp.route("/delete/<int:id>")
def delete(id):
    responsable = Responsable.get_by_id(id)
    responsable.delete()
    return redirect(url_for('responsable.index'))
