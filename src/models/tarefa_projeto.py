from . import db
from datetime import datetime

class TarefaProjeto(db.Model):
    __tablename__ = "tarefas_projeto"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data_inicio_prevista = db.Column(db.Date)
    data_fim_prevista = db.Column(db.Date)
    data_conclusao_real = db.Column(db.Date)
    
    projeto_id = db.Column(db.Integer, db.ForeignKey("projetos.id"), nullable=False)
    responsavel_id = db.Column(db.Integer, db.ForeignKey("usuarios.id")) # Pode ser um usuário interno ou um terceirizado (a ser definido como lidar com terceirizados)
    status_tarefa_id = db.Column(db.Integer, db.ForeignKey("status_tarefa.id"), nullable=False)

    # Relacionamentos
    projeto = db.relationship("Projeto", back_populates="tarefas")
    responsavel = db.relationship("Usuario", back_populates="tarefas_responsaveis")
    status_tarefa = db.relationship("StatusTarefa", back_populates="tarefas_projeto")

    def __repr__(self):
        return f'<TarefaProjeto {self.id}: {self.descricao[:50]}>'

