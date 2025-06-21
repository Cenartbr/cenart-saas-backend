from . import db
from datetime import datetime

class CentroCusto(db.Model):
    __tablename__ = "centros_custo"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False) # Ex: Produção, Criação e Desenvolvimento, Administrativo
    contas_pagar = db.relationship("ContaPagar", back_populates="centro_custo")

    def __repr__(self):
        return f'<CentroCusto {self.nome}>'

class Fornecedor(db.Model):
    __tablename__ = "fornecedores"
    id = db.Column(db.Integer, primary_key=True)
    nome_razao_social = db.Column(db.String(200), nullable=False, unique=True)
    cnpj_cpf = db.Column(db.String(20), unique=True, index=True)
    contato_nome = db.Column(db.String(150))
    contato_email = db.Column(db.String(150))
    contato_telefone = db.Column(db.String(30))
    # endereco_id = db.Column(db.Integer, db.ForeignKey("enderecos.id")) # Opcional, se quiser registrar endereço do fornecedor
    # endereco = db.relationship("Endereco")
    contas_pagar = db.relationship("ContaPagar", back_populates="fornecedor")

    def __repr__(self):
        return f'<Fornecedor {self.nome_razao_social}>'

class ContaPagar(db.Model):
    __tablename__ = "contas_pagar"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_emissao = db.Column(db.Date, default=datetime.utcnow)
    data_vencimento = db.Column(db.Date, nullable=False)
    data_pagamento = db.Column(db.Date)
    observacao = db.Column(db.Text)
    numero_documento = db.Column(db.String(100)) # Para NF, boleto, etc.
    parcela_atual = db.Column(db.Integer, default=1)
    total_parcelas = db.Column(db.Integer, default=1)

    status_conta_id = db.Column(db.Integer, db.ForeignKey("status_conta.id"), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey("fornecedores.id")) # Pode ser nulo para despesas internas sem fornecedor específico
    projeto_id = db.Column(db.Integer, db.ForeignKey("projetos.id")) # Se a despesa está vinculada a um projeto
    centro_custo_id = db.Column(db.Integer, db.ForeignKey("centros_custo.id"))
    # lancamento_caixa_id = db.Column(db.Integer, db.ForeignKey("lancamentos_caixa.id")) # Vinculo com o lançamento no caixa

    # Relacionamentos
    status_conta = db.relationship("StatusConta", back_populates="contas_pagar")
    fornecedor = db.relationship("Fornecedor", back_populates="contas_pagar")
    projeto = db.relationship("Projeto") # Não tem back_populates direto se projeto não armazena contas_pagar
    centro_custo = db.relationship("CentroCusto", back_populates="contas_pagar")
    # lancamento_caixa = db.relationship("LancamentoCaixa")

    def __repr__(self):
        return f'<ContaPagar {self.id}: {self.descricao[:50]} - R${self.valor}>'

