from flask import request, redirect, url_for, Blueprint

from models.doctores_model import Doctor
from views import doctores_view

doctor_bp = Blueprint('doctor', __name__, url_prefix="/doctores")

@doctor_bp.route("/")
def index():
    # Recupera todos los registros de usuarios
    doctores = Doctor.get_all()
    return doctores_view.list(doctores)
    
@doctor_bp.route("/create", methods = ['GET','POST'])
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
        direccion =request.form[' direccion']
        ciudad = request.form['ciudad']     
        correo = request.form['correo']    
        id_turno = request.form['id_turno']
        
        
        doctor = Doctor(ci, nombre, ap_paterno, ap_materno, fecha_nacimiento, sexo, telefono, direccion, ciudad, correo, id_turno)
        doctor.save()
        return redirect(url_for('doctores.index'))
    return doctores_view.create()

@doctor_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    doctor = Doctor.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        ci = request.form['ci']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        fecha_nacimiento = request.form['fecha_nacimiento']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        direccion =request.form[' direccion']
        ciudad = request.form['ciudad']     
        correo = request.form['correo']    
        id_turno = request.form['id_turno']
        
        #actualizar 
        doctor.update(ci=ci, nombre=nombre, ap_paterno=ap_paterno, ap_materno=ap_materno, fecha_nacimiento=fecha_nacimiento, sexo=sexo, telefono=telefono, direccion=direccion, ciudad=ciudad, correo=correo, id_turno=id_turno)
        return redirect(url_for('doctores.index'))
    return doctores_view.edit(doctor)

@doctor_bp.route("/delete/<int:id>")
def delete(id):
    
    doctor = Doctor.get_by_id(id)
    doctor.delete()
    return redirect(url_for('doctores.index'))

