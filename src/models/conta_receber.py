from . import db
from datetime import datetime

class ContaReceber(db.Model):
    __tablename__ = "contas_receber"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)
    valor_recebido = db.Column(db.Numeric(10, 2), default=0.0)
    data_emissao = db.Column(db.Date, default=datetime.utcnow)
    data_vencimento = db.Column(db.Date, nullable=False)
    data_recebimento = db.Column(db.Date)
    observacao = db.Column(db.Text)
    numero_documento = db.Column(db.String(100)) # Para NF, etc.
    parcela_atual = db.Column(db.Integer, default=1)
    total_parcelas = db.Column(db.Integer, default=1)

    status_conta_id = db.Column(db.Integer, db.ForeignKey("status_conta.id"), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey("projetos.id")) # Se o recebimento está vinculado a um projeto
    # orcamento_id = db.Column(db.Integer, db.ForeignKey("orcamentos.id")) # Se o recebimento está vinculado a um orçamento
    # lancamento_caixa_id = db.Column(db.Integer, db.ForeignKey("lancamentos_caixa.id"))

    # Relacionamentos
    status_conta = db.relationship("StatusConta", back_populates="contas_receber")
    cliente = db.relationship("Cliente") # Não tem back_populates direto se cliente não armazena contas_receber
    projeto = db.relationship("Projeto") # Não tem back_populates direto se projeto não armazena contas_receber
    # orcamento = db.relationship("Orcamento")
    # lancamento_caixa = db.relationship("LancamentoCaixa")

    def __repr__(self):
        return f'<ContaReceber {self.id}: {self.descricao[:50]} - R${self.valor_total}>'

