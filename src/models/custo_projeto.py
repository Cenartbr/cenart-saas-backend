from . import db
from datetime import datetime

class CustoProjeto(db.Model):
    __tablename__ = "custos_projeto"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_custo = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    observacao = db.Column(db.Text)

    projeto_id = db.Column(db.Integer, db.ForeignKey("projetos.id"), nullable=False)
    tipo_custo_id = db.Column(db.Integer, db.ForeignKey("tipos_custo.id"), nullable=False)
    # Poderia ter um relacionamento com Fornecedor se o custo for de um terceiro específico
    # fornecedor_id = db.Column(db.Integer, db.ForeignKey("fornecedores.id"))

    # Relacionamentos
    projeto = db.relationship("Projeto", back_populates="custos_projeto")
    tipo_custo = db.relationship("TipoCusto", back_populates="custos_projeto")
    # fornecedor = db.relationship("Fornecedor")

    def __repr__(self):
        return f'<CustoProjeto {self.id}: {self.descricao[:50]} - R${self.valor}>'

