from . import db

class StatusProjeto(db.Model):
    __tablename__ = "status_projeto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False) # Ex: Orçamento, Em Andamento, Pausado, Concluído, Cancelado

    # Relacionamento com Projetos
    projetos = db.relationship("Projeto", back_populates="status_projeto")

    def __repr__(self):
        return f'<StatusProjeto {self.nome}>'

