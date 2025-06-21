from . import db

class Funcionario(db.Model):
    __tablename__ = "funcionarios"

    id = db.Column(db.Integer, primary_key=True)
    # Chave estrangeira para Usuario, assumindo que todo funcionário é um usuário do sistema
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), unique=True, nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    data_admissao = db.Column(db.Date)
    salario_base = db.Column(db.Numeric(10, 2))
    vale_alimentacao = db.Column(db.Numeric(10, 2), default=0.0)
    outros_beneficios = db.Column(db.Text) # Descrição de outros benefícios
    is_ativo = db.Column(db.Boolean, default=True)

    # Relacionamento com Usuario
    usuario = db.relationship("Usuario", back_populates="funcionario_info")

    def __repr__(self):
        return f'<Funcionario {self.usuario.nome if self.usuario else "N/A"} - Cargo: {self.cargo}>'

class Terceirizado(db.Model):
    __tablename__ = "terceirizados"

    id = db.Column(db.Integer, primary_key=True)
    nome_razao_social = db.Column(db.String(200), nullable=False, unique=True)
    cnpj_cpf = db.Column(db.String(20), unique=True, index=True)
    especialidade = db.Column(db.String(150)) # Ex: Escultor, Arquiteto, Eletricista
    contato_nome = db.Column(db.String(150))
    contato_email = db.Column(db.String(150))
    contato_telefone = db.Column(db.String(30))
    observacoes = db.Column(db.Text)
    # Poderia ter um relacionamento com TarefaProjeto se um terceirizado for responsável por tarefas
    # ou com CustoProjeto se os custos de terceirizados forem lançados diretamente.

    def __repr__(self):
        return f'<Terceirizado {self.nome_razao_social}>'

