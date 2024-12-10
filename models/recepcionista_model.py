from database import db
class Recepcionista(db.Model):
    __tablename__ = "recepcionistas"

    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    ap_paterno = db.Column(db.String(100), nullable=False)
    ap_materno = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    ciudad = db.Column(db.String(100))
    correo = db.Column(db.String(150), unique=True)
    id_turno = db.Column(db.Integer, db.ForeignKey('turnos.id'), nullable=False)
    
    def __init__(self, ci, nombre, ap_paterno, ap_materno, fecha_nacimiento, sexo, telefono, direccion, ciudad, correo, id_turno):
        self.ci = ci
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.correo = correo
        self.id_turno = id_turno

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Recepcionista.query.all()

    @staticmethod
    def get_by_id(id):
        return Recepcionista.query.get(id)

    def update(self, ci=None, nombre=None, ap_paterno=None, ap_materno=None, fecha_nacimiento=None, sexo=None, telefono=None, direccion=None, ciudad=None, correo=None, id_turno=None):
        if ci:
            self.ci = ci
        if nombre:
            self.nombre = nombre
        if ap_paterno:
            self.ap_paterno = ap_paterno
        if ap_materno:
            self.ap_materno = ap_materno
        if fecha_nacimiento:
            self.fecha_nacimiento = fecha_nacimiento
        if sexo:
            self.sexo = sexo
        if telefono:
            self.telefono = telefono
        if direccion:
            self.direccion = direccion
        if ciudad:
            self.ciudad = ciudad
        if correo:
            self.correo = correo
        if id_turno:
            self.id_turno = id_turno
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()