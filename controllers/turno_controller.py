from flask import request, redirect, url_for, Blueprint

from models.turno_model import Turno
from views import turno_view

turno_bp = Blueprint('turno', __name__, url_prefix="/turnos")

@turno_bp.route("/")
def index():
    # Recupera todos los registros de turnos
    turnos = Turno.get_all()
    return turno_view.list(turnos)

@turno_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        
        turno = Turno(nombre)
        turno.save()
        return redirect(url_for('turno.index'))
    return turno_view.create()

@turno_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    turno = Turno.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        
        # Actualiza los datos del turno
        turno.update(nombre=nombre)
        return redirect(url_for('turno.index'))
    return turno_view.edit(turno)

@turno_bp.route("/delete/<int:id>")
def delete(id):
    turno = Turno.get_by_id(id)
    turno.delete()
    return redirect(url_for('turno.index'))
