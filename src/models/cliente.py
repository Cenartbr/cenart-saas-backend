from . import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome_razao_social = db.Column(db.String(200), nullable=False)
    cnpj_cpf = db.Column(db.String(20), unique=True, index=True)
    # Chave estrangeira para Endereco
    endereco_id = db.Column(db.Integer, db.ForeignKey("enderecos.id"))
    # Chave estrangeira para Contato (contato principal)
    # Um cliente pode ter vários contatos, mas um pode ser o principal.
    # Se for uma relação de um para muitos, o contato principal pode ser um campo separado ou uma flag no modelo Contato.
    # Para simplificar, vamos assumir que um cliente tem um endereço principal e pode ter vários contatos.
    
    # Relacionamentos
    endereco = db.relationship("Endereco", back_populates="clientes", uselist=False) # Um cliente tem um endereço
    contatos = db.relationship("Contato", back_populates="cliente", cascade="all, delete-orphan")
    projetos = db.relationship("Projeto", back_populates="cliente", cascade="all, delete-orphan")
    orcamentos = db.relationship("Orcamento", back_populates="cliente", cascade="all, delete-orphan")
    # contas_receber = db.relationship("ContaReceber", back_populates="cliente") # Se uma conta a receber pode ser diretamente do cliente sem projeto

    def __repr__(self):
        return f'<Cliente {self.nome_razao_social}>'

