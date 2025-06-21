from . import db

class StatusConta(db.Model):
    __tablename__ = "status_conta"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False) # Ex: A Pagar, Pago, Vencido, A Receber, Recebido

    # Relacionamentos
    contas_pagar = db.relationship("ContaPagar", back_populates="status_conta")
    contas_receber = db.relationship("ContaReceber", back_populates="status_conta")

    def __repr__(self):
        return f'<StatusConta {self.nome}>'

