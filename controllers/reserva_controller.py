from flask import request, redirect, url_for, Blueprint

from models.reserva_model import Reserva
from views import reserva_view

reserva_bp = Blueprint('reserva', __name__, url_prefix="/reserva")

@reserva_bp.route("/")
def index():
    # Recupera todos los registros de reservas
    reservas = Reserva.get_all()
    return reserva_view.list(reservas)

@reserva_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        id_paciente = request.form['id_paciente']
        id_doctor = request.form['id_doctor']
        fecha_reserva = request.form['fecha_reserva']
        hora_reserva = request.form['hora_reserva']
        
        reserva = Reserva(id_paciente, id_doctor, fecha_reserva, hora_reserva)
        reserva.save()
        return redirect(url_for('reserva.index'))
    return reserva_view.create()

@reserva_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    reserva = Reserva.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        id_paciente = request.form['id_paciente']
        id_doctor = request.form['id_doctor']
        fecha_reserva = request.form['fecha_reserva']
        hora_reserva = request.form['hora_reserva']
        
        # Actualiza los datos de la reserva
        reserva.update(id_paciente=id_paciente, id_doctor=id_doctor, fecha_reserva=fecha_reserva, hora_reserva=hora_reserva)
        return redirect(url_for('reserva.index'))
    return reserva_view.edit(reserva)

@reserva_bp.route("/delete/<int:id>")
def delete(id):
    reserva = Reserva.get_by_id(id)
    reserva.delete()
    return redirect(url_for('reserva.index'))
