from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    senha_hash = db.Column(db.String(256), nullable=False)
    papel_id = db.Column(db.Integer, db.ForeignKey("papeis.id"), nullable=False)

    # Relacionamento com Papel
    papel = db.relationship("Papel", back_populates="usuarios")
    
    # Relacionamento com Funcionarios (um para um, se um usuário é sempre um funcionário)
    # Se nem todo usuário é um funcionário, este relacionamento pode ser opcional ou estar na tabela Funcionarios
    funcionario_info = db.relationship("Funcionario", back_populates="usuario", uselist=False) # uselist=False para one-to-one

    # Relacionamento com TarefasProjeto (um usuário pode ser responsável por muitas tarefas)
    tarefas_responsaveis = db.relationship("TarefaProjeto", back_populates="responsavel")

    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f'<Usuario {self.nome} ({self.email})>'

