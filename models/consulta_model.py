from database import db

class Consulta(db.Model):
    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)
    id_doctor = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    sintomas = db.Column(db.String(255))
    diagnostico = db.Column(db.String(255))
    
    #Relaciones con doctores
    #doctores = db.relationship('Doctor', back_populates = 'consultas')
    #pacientes = db.relationship('Paciente', back_populates = 'consultas')
    #recetas = db.relationship('Recetas', back_populates = 'consulta')

    def __init__(self, id_doctor, id_paciente, fecha, hora, sintomas, diagnostico):
        self.id_doctor = id_doctor
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.hora = hora
        self.sintomas = sintomas
        self.diagnostico = diagnostico

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Consulta.query.all()

    @staticmethod
    def get_by_id(id):
        return Consulta.query.get(id)

    def update(self, id_doctor=None, id_paciente=None, fecha=None, hora=None, sintomas=None, diagnostico=None):
        if id_doctor:
            self.id_doctor = id_doctor
        if id_paciente:
            self.id_paciente = id_paciente
        if fecha:
            self.fecha = fecha
        if hora:
            self.hora = hora
        if sintomas:
            self.sintomas = sintomas
        if diagnostico:
            self.diagnostico = diagnostico
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
