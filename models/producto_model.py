from database import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_adquirido = db.Column(db.Date, nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(100))
    precio = db.Column(db.Float, nullable=False)
    id_recepcionista = db.Column(db.Integer, db.ForeignKey('recepcionistas.id'), nullable=False)
    
    #Relaciiones
    #recepcionista = db.relationship('Recepcionista', back_populates ='productos')
    
    def __init__(self, nombre, fecha_adquirido, fecha_vencimiento, cantidad, marca, precio, id_recepcionista):
        self.nombre = nombre
        self.fecha_adquirido = fecha_adquirido
        self.fecha_vencimiento = fecha_vencimiento
        self.cantidad = cantidad
        self.marca = marca
        self.precio = precio
        self.id_recepcionista = id_recepcionista

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Producto.query.all()

    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)

    def update(self, nombre=None, fecha_adquirido=None, fecha_vencimiento=None, cantidad=None, marca=None, precio=None):
        if nombre:
            self.nombre = nombre
        if fecha_adquirido:
            self.fecha_adquirido = fecha_adquirido
        if fecha_vencimiento:
            self.fecha_vencimiento = fecha_vencimiento
        if cantidad:
            self.cantidad = cantidad
        if marca:
            self.marca = marca
        if precio:
            self.precio = precio
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()