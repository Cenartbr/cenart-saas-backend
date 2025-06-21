from . import db

class ItemOrcamento(db.Model):
    __tablename__ = "itens_orcamento"

    id = db.Column(db.Integer, primary_key=True)
    descricao_item = db.Column(db.Text, nullable=False)
    quantidade = db.Column(db.Numeric(10, 2), nullable=False, default=1)
    unidade_medida = db.Column(db.String(50)) # Ex: Un, m², Kg, Hora
    custo_unitario_estimado = db.Column(db.Numeric(10, 2), default=0.0)
    preco_venda_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal_custo = db.Column(db.Numeric(10, 2), default=0.0) # quantidade * custo_unitario_estimado
    subtotal_venda = db.Column(db.Numeric(10, 2), nullable=False) # quantidade * preco_venda_unitario
    observacoes = db.Column(db.Text)

    orcamento_id = db.Column(db.Integer, db.ForeignKey("orcamentos.id"), nullable=False)
    # material_id = db.Column(db.Integer, db.ForeignKey("materiais.id")) # Se o item for um material específico

    # Relacionamentos
    orcamento = db.relationship("Orcamento", back_populates="itens_orcamento")
    # material = db.relationship("Material")

    def __repr__(self):
        return f'<ItemOrcamento {self.id}: {self.descricao_item[:50]} - Qtd: {self.quantidade}>'

