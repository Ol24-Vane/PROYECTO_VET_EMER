from database import db

class Receta(db.Model):
    __tablename__ = "recetas"

    id = db.Column(db.Integer, primary_key=True)
    id_consulta = db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=False)
    medicamento = db.Column(db.String(100), nullable=False)
    dosis = db.Column(db.String(50), nullable=False)
    indicaciones = db.Column(db.String(255), nullable=False)
    
    #Relaciones con consultas
    #consulta = db.relationship('Consulta', back_populates = 'recetas')


    def __init__(self, id_consulta, medicamento, dosis, indicaciones):
        self.id_consulta = id_consulta
        self.medicamento = medicamento
        self.dosis = dosis
        self.indicaciones = indicaciones

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Receta.query.all()

    @staticmethod
    def get_by_id(id):
        return Receta.query.get(id)

    def update(self, medicamento=None, dosis=None, indicaciones=None):
        if medicamento:
            self.medicamento = medicamento
        if dosis:
            self.dosis = dosis
        if indicaciones:
            self.indicaciones = indicaciones
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
