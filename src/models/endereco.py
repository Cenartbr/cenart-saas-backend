from . import db
from datetime import datetime

class Endereco(db.Model):
    __tablename__ = "enderecos"

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    
    # Relacionamentos
    clientes = db.relationship("Cliente", back_populates="endereco")
    
    def __repr__(self):
        return f'<Endereco {self.logradouro}, {self.numero} - {self.cidade}/{self.estado}>'
