from flask import request, redirect, url_for, Blueprint

from models.paciente_model import Paciente
from views import paciente_view

paciente_bp = Blueprint('paciente', __name__, url_prefix="/paciente")

@paciente_bp.route("/")
def index():
    # Recupera todos los registros de pacientes
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)

@paciente_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        edad = request.form['edad']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        
        paciente = Paciente(nombre, edad, sexo, direccion, ciudad, telefono, fecha_nacimiento)
        paciente.save()
        return redirect(url_for('paciente.index'))
    return paciente_view.create()

@paciente_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    paciente = Paciente.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        edad = request.form['edad']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        
        # Actualiza los datos del paciente
        paciente.update(nombre=nombre, edad=edad, sexo=sexo, direccion=direccion, ciudad=ciudad, telefono=telefono, fecha_nacimiento=fecha_nacimiento)
        return redirect(url_for('paciente.index'))
    return paciente_view.edit(paciente)

@paciente_bp.route("/delete/<int:id>")
def delete(id):
    paciente = Paciente.get_by_id(id)
    paciente.delete()
    return redirect(url_for('paciente.index'))
