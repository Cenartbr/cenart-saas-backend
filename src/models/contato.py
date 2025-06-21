from . import db

class Contato(db.Model):
    __tablename__ = "contatos"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150))
    telefone = db.Column(db.String(30))
    cargo = db.Column(db.String(100)) # Cargo do contato na empresa cliente
    is_principal = db.Column(db.Boolean, default=False) # Flag para indicar se é o contato principal

    # Relacionamento com Cliente
    cliente = db.relationship("Cliente", back_populates="contatos")

    def __repr__(self):
        return f'<Contato {self.nome} (Cliente: {self.cliente.nome_razao_social if self.cliente else "N/A"})>'

