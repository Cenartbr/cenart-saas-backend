from . import db

class Papel(db.Model):
    __tablename__ = "papeis"

    id = db.Column(db.Integer, primary_key=True)
    nome_papel = db.Column(db.String(80), unique=True, nullable=False)
    # Relacionamento com Usuarios
    usuarios = db.relationship("Usuario", back_populates="papel")

    def __repr__(self):
        return f'<Papel {self.nome_papel}>'

