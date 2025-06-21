from . import db

class StatusTarefa(db.Model):
    __tablename__ = "status_tarefa"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False) # Ex: A Fazer, Em Andamento, Concluída, Bloqueada

    # Relacionamento com TarefasProjeto
    tarefas_projeto = db.relationship("TarefaProjeto", back_populates="status_tarefa")

    def __repr__(self):
        return f'<StatusTarefa {self.nome}>'

