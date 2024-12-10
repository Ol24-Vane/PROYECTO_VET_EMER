from flask import request, redirect, url_for, Blueprint

from models.consulta_model import Consulta
from views import consulta_view

consulta_bp = Blueprint('consulta', __name__, url_prefix="/consulta")

@consulta_bp.route("/")
def index():
    # Recupera todos los registros de consultas
    consultas = Consulta.get_all()
    return consulta_view.list(consultas)

@consulta_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        id_paciente = request.form['id_paciente']
        id_doctor = request.form['id_doctor']
        fecha_consulta = request.form['fecha_consulta']
        hora_consulta = request.form['hora_consulta']
        sintomas = request.form['sintomas']
        
        consulta = Consulta(id_paciente, id_doctor, fecha_consulta, hora_consulta, sintomas)
        consulta.save()
        return redirect(url_for('consulta.index'))
    return consulta_view.create()

@consulta_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    consulta = Consulta.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        id_paciente = request.form['id_paciente']
        id_doctor = request.form['id_doctor']
        fecha_consulta = request.form['fecha_consulta']
        hora_consulta = request.form['hora_consulta']
        sintomas = request.form['sintomas']
        
        # Actualiza los datos de la consulta
        consulta.update(id_paciente=id_paciente, id_doctor=id_doctor, fecha_consulta=fecha_consulta, hora_consulta=hora_consulta, sintomas=sintomas)
        return redirect(url_for('consulta.index'))
    return consulta_view.edit(consulta)

@consulta_bp.route("/delete/<int:id>")
def delete(id):
    consulta = Consulta.get_by_id(id)
    consulta.delete()
    return redirect(url_for('consulta.index'))
