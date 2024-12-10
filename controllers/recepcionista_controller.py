from flask import request, redirect, url_for, Blueprint

from models.recepcionista_model import Recepcionista
from models.turno_model import Turno
from views import recepcionista_view

recepcionista_bp = Blueprint('recepcionistas', __name__, url_prefix="/recepcionistas")

@recepcionista_bp.route("/")
def index():
    # Recupera todos los registros de recepcionistas
    recepcionistas = Recepcionista.get_all()
    return recepcionista_view.list(recepcionistas)

@recepcionista_bp.route("/create", methods = ['GET','POST'])
def create():
    
    if request.method == 'POST':
        # Recupera los datos del formulario
        ci = request.form['ci']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        fecha_nacimiento = request.form['fecha_nacimiento']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']     
        correo = request.form['correo']    
        
        recepcionista = Recepcionista(ci, nombre, ap_paterno, ap_materno, fecha_nacimiento, sexo, telefono, direccion, ciudad, correo)
        recepcionista.save()
        return redirect(url_for('recepcionistas.index'))
    return recepcionista_view.create()

@recepcionista_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    recepcionista = Recepcionista.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        ci = request.form['ci']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        fecha_nacimiento = request.form['fecha_nacimiento']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        direccion =request.form['direccion']
        ciudad = request.form['ciudad']     
        correo = request.form['correo']    
        
        # Actualiza los datos del recepcionista
        recepcionista.update(ci=ci, nombre=nombre, ap_paterno=ap_paterno, ap_materno=ap_materno, fecha_nacimiento=fecha_nacimiento, sexo=sexo, telefono=telefono, direccion=direccion, ciudad=ciudad, correo=correo)
        return redirect(url_for('recepcionistas.index'))
    return recepcionista_view.edit(recepcionista)

@recepcionista_bp.route("/delete/<int:id>")
def delete(id):
    recepcionista = Recepcionista.get_by_id(id)
    recepcionista.delete()
    return redirect(url_for('recepcionistas.index'))
