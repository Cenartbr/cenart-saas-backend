from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here to ensure they are known to SQLAlchemy
from .papel import Papel
from .usuario import Usuario
from .endereco import Endereco
from .cliente import Cliente
from .contato import Contato
from .status_projeto import StatusProjeto
from .projeto import Projeto
from .status_tarefa import StatusTarefa
from .tarefa_projeto import TarefaProjeto
from .tipo_custo import TipoCusto
from .custo_projeto import CustoProjeto
from .status_conta import StatusConta
from .conta_pagar import CentroCusto, Fornecedor, ContaPagar # CentroCusto and Fornecedor are in conta_pagar.py
from .conta_receber import ContaReceber
from .status_orcamento import StatusOrcamento
from .orcamento import Orcamento
from .item_orcamento import ItemOrcamento
from .material import Material
from .equipe import Funcionario, Terceirizado # Funcionario and Terceirizado are in equipe.py
from .financeiro_aux import ContaBancaria, LancamentoCaixa # ContaBancaria and LancamentoCaixa are in financeiro_aux.py

