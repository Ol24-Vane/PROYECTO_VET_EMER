from database import db

class Turno(db.Model):
    __tablename__ = "turnos"
    id = db.Column(db.Integer, primary_key=True)
    turno = db.Column(db.String(50), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_final = db.Column(db.Time, nullable=False)
    
    #Relacion con turnos
    #doctores = db.relationship('Doctor', back_populates = 'turno')
    #recepcionitas = db.relationship('Recepcionista', back_populates = 'turnos')

    def __init__(self, turno, hora_inicio, hora_final):
        self.turno = turno
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Turno.query.all()

    @staticmethod
    def get_by_id(id):
        return Turno.query.get(id)
    
    

    def update(self, turno=None, hora_inicio=None, hora_final=None):
        if turno:
            self.turno = turno
        if hora_inicio:
            self.hora_inicio = hora_inicio
        if hora_final:
            self.hora_final = hora_final
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()