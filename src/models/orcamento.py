from . import db
from datetime import datetime

class Orcamento(db.Model):
    __tablename__ = "orcamentos"

    id = db.Column(db.Integer, primary_key=True)
    codigo_orcamento = db.Column(db.String(50), unique=True, nullable=False, index=True) # Ex: ORC-2024-001
    data_criacao = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    data_validade = db.Column(db.Date)
    valor_total_estimado = db.Column(db.Numeric(12, 2), default=0.0)
    valor_total_final = db.Column(db.Numeric(12, 2)) # Preenchido após aprovação ou ajuste
    observacoes_internas = db.Column(db.Text)
    condicoes_pagamento = db.Column(db.Text)
    prazo_entrega_estimado = db.Column(db.String(100))

    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    responsavel_comercial_id = db.Column(db.Integer, db.ForeignKey("usuarios.id")) # Usuário que criou o orçamento
    status_orcamento_id = db.Column(db.Integer, db.ForeignKey("status_orcamento.id"), nullable=False)
    projeto_gerado_id = db.Column(db.Integer, db.ForeignKey("projetos.id"), unique=True) # Se o orçamento foi convertido em projeto

    # Relacionamentos
    cliente = db.relationship("Cliente", back_populates="orcamentos")
    responsavel_comercial = db.relationship("Usuario") # Não necessita back_populates se Usuario não armazena orçamentos diretamente
    status_orcamento = db.relationship("StatusOrcamento", back_populates="orcamentos")
    itens_orcamento = db.relationship("ItemOrcamento", back_populates="orcamento", cascade="all, delete-orphan")
    projeto_gerado = db.relationship("Projeto", foreign_keys=[projeto_gerado_id]) # Relação um-para-um com Projeto

    def __repr__(self):
        return f'<Orcamento {self.codigo_orcamento} - Cliente: {self.cliente.nome_razao_social if self.cliente else "N/A"}>'

