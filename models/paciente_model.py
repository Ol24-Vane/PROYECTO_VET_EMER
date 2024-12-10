from database import db

class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50))
    rasgos = db.Column(db.String(255))
    id_responsable = db.Column(db.Integer, db.ForeignKey('responsables.id'), nullable=False)

    #Relaciones con reservas
    #reservas = db.relationship('Reserva', back_populates ='paciente')
    #consultas = db.relationship('Consulta', back_populates = 'pacientes')
    #responsable = db.relationship('Responsable', back_populates = 'pacientes')
    
    def __init__(self, nombre, raza, edad, color, rasgos, id_responsable):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.rasgos = rasgos
        self.id_responsable = id_responsable

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()

    @staticmethod
    def get_by_id(id):
        return Paciente.query.get(id)

    def update(self, nombre=None, raza=None, edad=None, color=None, rasgos=None):
        if nombre:
            self.nombre = nombre
        if raza:
            self.raza = raza
        if edad:
            self.edad = edad
        if color:
            self.color = color
        if rasgos:
            self.rasgos = rasgos
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
