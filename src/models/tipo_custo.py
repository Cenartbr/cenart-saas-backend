from . import db

class TipoCusto(db.Model):
    __tablename__ = "tipos_custo"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False) # Ex: Material, Mão de Obra, Terceirizado, Despesa Administrativa
    descricao = db.Column(db.Text)

    # Relacionamento com CustosProjeto
    custos_projeto = db.relationship("CustoProjeto", back_populates="tipo_custo")

    def __repr__(self):
        return f'<TipoCusto {self.nome}>'

