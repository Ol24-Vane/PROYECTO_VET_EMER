from flask import Flask ,redirect, url_for, session,request, render_template
from controllers import usuario_controller
from controllers import turno_controller
from controllers import doctores_controller
from controllers import consulta_controller
from controllers import paciente_controller
from controllers import producto_controller
from controllers import recepcionista_controller
from controllers import receta_controller
from controllers import reserva_controller
from controllers import responsable_controller
from controllers import auth
from database import db



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///veterinaria.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'mi_clave_secreta'


db.init_app(app)

app.register_blueprint(auth.auth_bp)
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(doctores_controller.doctor_bp)
app.register_blueprint(turno_controller.turno_bp)
app.register_blueprint(consulta_controller.consulta_bp)
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(recepcionista_controller.recepcionista_bp)
app.register_blueprint(receta_controller.receta_bp)
app.register_blueprint(reserva_controller.reserva_bp)
app.register_blueprint(responsable_controller.responsable_bp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active'if request.path == path else ''
    return dict(is_active = is_active)

@app.route("/")
def home():
    if 'user_id' not in session:
        return redirect(url_for('auths.login'))
    # Redirige según el rol
    if session.get('rol') == 'admin':
        return redirect(url_for('usuario.index'))
    return redirect(url_for('usuario.index'))


#@app.route("/")
#def home():
#    return render_template('auths/login.html')#"<h1> Aplicacion ventas</h1>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Turnos creados exitosamente")
    app.run(debug=True)