from flask import request, redirect, url_for, Blueprint

from models.receta_model import Receta
from views import receta_view

receta_bp = Blueprint('receta', __name__, url_prefix="/receta")

@receta_bp.route("/")
def index():
    # Recupera todos los registros de recetas
    recetas = Receta.get_all()
    return receta_view.list(recetas)

@receta_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # Recupera los datos del formulario
        id_paciente = request.form['id_paciente']
        fecha_receta = request.form['fecha_receta']
        medicamentos = request.form['medicamentos']
        
        receta = Receta(id_paciente, fecha_receta, medicamentos)
        receta.save()
        return redirect(url_for('receta.index'))
    return receta_view.create()

@receta_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    receta = Receta.get_by_id(id)
    if request.method == 'POST':
        # Recupera los datos del formulario
        id_paciente = request.form['id_paciente']
        fecha_receta = request.form['fecha_receta']
        medicamentos = request.form['medicamentos']
        
        # Actualiza los datos de la receta
        receta.update(id_paciente=id_paciente, fecha_receta=fecha_receta, medicamentos=medicamentos)
        return redirect(url_for('receta.index'))
    return receta_view.edit(receta)

@receta_bp.route("/delete/<int:id>")
def delete(id):
    receta = Receta.get_by_id(id)
    receta.delete()
    return redirect(url_for('receta.index'))
