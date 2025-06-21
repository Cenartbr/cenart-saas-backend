from . import db
from datetime import datetime

class ContaBancaria(db.Model):
    __tablename__ = "contas_bancarias"
    id = db.Column(db.Integer, primary_key=True)
    nome_banco = db.Column(db.String(100), nullable=False)
    agencia = db.Column(db.String(20))
    numero_conta = db.Column(db.String(30), nullable=False, unique=True)
    tipo_conta = db.Column(db.String(50)) # Ex: Corrente, Poupança, Caixa
    saldo_inicial = db.Column(db.Numeric(12, 2), default=0.0)
    data_saldo_inicial = db.Column(db.Date, default=datetime.utcnow)
    # Relacionamento com LancamentosCaixa
    lancamentos_caixa = db.relationship("LancamentoCaixa", back_populates="conta_bancaria")

    def __repr__(self):
        return f'<ContaBancaria {self.nome_banco} - {self.numero_conta}>'

class LancamentoCaixa(db.Model):
    __tablename__ = "lancamentos_caixa"

    id = db.Column(db.Integer, primary_key=True)
    data_lancamento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    descricao = db.Column(db.Text, nullable=False)
    tipo_lancamento = db.Column(db.String(10), nullable=False) # "Entrada" ou "Saida"
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    observacao = db.Column(db.Text)
    conciliado = db.Column(db.Boolean, default=False)
    data_conciliacao = db.Column(db.DateTime)

    conta_bancaria_id = db.Column(db.Integer, db.ForeignKey("contas_bancarias.id"), nullable=False)
    # Chaves estrangeiras opcionais para vincular o lançamento à sua origem
    conta_pagar_id = db.Column(db.Integer, db.ForeignKey("contas_pagar.id"))
    conta_receber_id = db.Column(db.Integer, db.ForeignKey("contas_receber.id"))
    # projeto_id = db.Column(db.Integer, db.ForeignKey("projetos.id")) # Se for um adiantamento/reembolso direto do projeto

    # Relacionamentos
    conta_bancaria = db.relationship("ContaBancaria", back_populates="lancamentos_caixa")
    # Se desejar referenciar diretamente a conta de origem:
    # conta_pagar_origem = db.relationship("ContaPagar", foreign_keys=[conta_pagar_id])
    # conta_receber_origem = db.relationship("ContaReceber", foreign_keys=[conta_receber_id])

    def __repr__(self):
        return f'<LancamentoCaixa {self.id}: {self.tipo_lancamento} R${self.valor} - {self.descricao[:50]}>'

