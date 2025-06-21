from . import db
from datetime import datetime

class Projeto(db.Model):
    __tablename__ = "projetos"

    id = db.Column(db.Integer, primary_key=True)
    nome_projeto = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.Date)
    data_prazo = db.Column(db.Date)
    orcamento_aprovado = db.Column(db.Numeric(10, 2)) # Ex: 12345.67
    
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    status_projeto_id = db.Column(db.Integer, db.ForeignKey("status_projeto.id"), nullable=False)

    # Relacionamentos
    cliente = db.relationship("Cliente", back_populates="projetos")
    status_projeto = db.relationship("StatusProjeto", back_populates="projetos")
    tarefas = db.relationship("TarefaProjeto", back_populates="projeto", cascade="all, delete-orphan")
    custos_projeto = db.relationship("CustoProjeto", back_populates="projeto", cascade="all, delete-orphan")
    # contas_receber = db.relationship("ContaReceber", back_populates="projeto") # Se uma conta a receber está sempre ligada a um projeto
    # orcamento_associado = db.relationship("Orcamento", back_populates="projeto_final") # Se um projeto é gerado a partir de um orçamento

    def __repr__(self):
        return f'<Projeto {self.nome_projeto}>'

