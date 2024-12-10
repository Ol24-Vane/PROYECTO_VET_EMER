from database import db

class Reserva(db.Model):
    __tablename__ = "reservas"

    id = db.Column(db.Integer, primary_key=True)
    id_responsable = db.Column(db.Integer, db.ForeignKey('responsables.id'), nullable=False)
    id_doctor = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    observacion = db.Column(db.String(255))
    
    #Relaciones
    #responsable = db.relationship('Responsable', back_populates = 'reservas')
    #doctores = db.relationship('Doctor', back_populates = 'reservas')

    def __init__(self, id_responsable, id_doctor, fecha, hora, observacion):
        self.id_responsable = id_responsable
        self.id_doctor = id_doctor
        self.fecha = fecha
        self.hora = hora
        self.observacion = observacion

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Reserva.query.all()

    @staticmethod
    def get_by_id(id):
        return Reserva.query.get(id)

    def update(self, id_responsable=None, id_doctor=None, fecha=None, hora=None, observacion=None):
        if id_responsable:
            self.id_responsable = id_responsable
        if id_doctor:
            self.id_doctor = id_doctor
        if fecha:
            self.fecha = fecha
        if hora:
            self.hora = hora
        if observacion:
            self.observacion = observacion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
