from . import db

class StatusOrcamento(db.Model):
    __tablename__ = "status_orcamento"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False) # Ex: Em Elaboração, Enviado, Aprovado, Rejeitado, Em Negociação, Convertido em Projeto

    # Relacionamento com Orcamentos
    orcamentos = db.relationship("Orcamento", back_populates="status_orcamento")

    def __repr__(self):
        return f'<StatusOrcamento {self.nome}>'

