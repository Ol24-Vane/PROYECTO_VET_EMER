from database import db

class Responsable(db.Model):
    __tablename__ = "responsables"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ap_paterno = db.Column(db.String(100), nullable=False)
    ap_materno = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    id_recepcionista = db.Column(db.Integer, db.ForeignKey('recepcionistas.id'), nullable=False)

    # Relación con la tabla `recepcionistas`
    #recepcionista = db.relationship('Recepcionista', back_populates = 'responsable')
    #pacientes = db.relationship('Paciente', back_populates = 'responsable')
    #reservas = db.relationship('Reserva', back_populates = 'responsable')

    def __init__(self, nombre, ap_paterno, ap_materno, fecha_nacimiento, sexo, telefono, direccion, ciudad, correo, id_recepcionista):
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.correo = correo
        self.id_recepcionista = id_recepcionista

    def save(self):
        """Guarda el objeto en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Obtiene todos los responsables."""
        return Responsable.query.all()

    @staticmethod
    def get_by_id(id):
        """Obtiene un responsable por su ID."""
        return Responsable.query.get(id)

    def update(self, nombre=None, ap_paterno=None, ap_materno=None, fecha_nacimiento=None, sexo=None, telefono=None, direccion=None, ciudad=None, correo=None, id_recepcionista=None):
        """Actualiza los datos del responsable."""
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
        if id_recepcionista:
            self.id_recepcionista = id_recepcionista
        db.session.commit()

    def delete(self):
        """Elimina el objeto de la base de datos."""
        db.session.delete(self)
        db.session.commit()
