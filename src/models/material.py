from . import db

class Material(db.Model):
    __tablename__ = "materiais"

    id = db.Column(db.Integer, primary_key=True)
    nome_material = db.Column(db.String(150), nullable=False, unique=True)
    descricao = db.Column(db.Text)
    unidade_medida = db.Column(db.String(50), nullable=False) # Ex: Un, m, m², Kg, L
    custo_medio_unitario = db.Column(db.Numeric(10, 2), default=0.0)
    saldo_estoque = db.Column(db.Numeric(10, 2), default=0.0)
    # fornecedor_padrao_id = db.Column(db.Integer, db.ForeignKey("fornecedores.id")) # Opcional

    # Relacionamentos
    # fornecedor_padrao = db.relationship("Fornecedor")
    # itens_orcamento = db.relationship("ItemOrcamento", back_populates="material") # Se ItemOrcamento tiver FK para Material

    def __repr__(self):
        return f'<Material {self.nome_material}>'

