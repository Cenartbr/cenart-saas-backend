"""
Main entry point for the cenart_saas_backend application.

This script initializes the Flask application, configures the database,
and registers all necessary blueprints for different modules of the SaaS.
"""
import sys
import os

# Add the project root to the Python path to allow absolute imports from 'src'
# This is crucial for Flask to find modules like 'src.models' or 'src.routes'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from src.models import db # Import db instance from src.models

# Import Blueprints
from src.routes.financeiro_routes import financeiro_bp
from src.routes.projetos_routes import projetos_bp
from src.routes.comercial_routes import comercial_bp
from src.routes.auth_routes import auth_bp # Importa o novo blueprint de autenticação

# Application Factory Function
def create_app(config_name=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, static_folder='static', static_url_path='')

    # --- Configuration --- 
    db_user = os.getenv('DB_USERNAME', 'root')
    db_password = os.getenv('DB_PASSWORD', 'password')
    db_host = os.getenv('DB_HOST', 'localhost') # Or your MySQL host
    db_port = os.getenv('DB_PORT', '3306')
    db_name = os.getenv("DB_NAME", "mydb") # It's good practice to use a specific DB name

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False # Set to True for debugging SQL queries

    # Initialize extensions
    db.init_app(app)

    # --- Register Blueprints --- 
    app.register_blueprint(financeiro_bp)
    app.register_blueprint(projetos_bp)
    app.register_blueprint(comercial_bp)
    app.register_blueprint(auth_bp) # Registra o blueprint de autenticação

    # --- Basic Routes (can be moved to a 'main_routes.py' blueprint) ---
    @app.route('/')
    def app_index():
        return jsonify({"message": "Bem-vindo à API do CENART SaaS!"})

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200

    with app.app_context():
        db.create_all()
        print(f"Database tables created/verified for {db_name}!")
        seed_initial_data(db)

    return app

def seed_initial_data(db_instance):
    """Seeds the database with initial necessary data like roles and statuses."""
    from src.models.papel import Papel
    from src.models.status_projeto import StatusProjeto
    from src.models.status_tarefa import StatusTarefa
    from src.models.status_conta import StatusConta
    from src.models.status_orcamento import StatusOrcamento
    from src.models.conta_pagar import CentroCusto # CentroCusto is in conta_pagar.py
    from src.models.usuario import Usuario # Importar Usuario para criar usuário de teste
    from werkzeug.security import generate_password_hash # Para hashear a senha

    # Seed Papéis (Roles)
    roles_data = ["Administrador", "Financeiro", "Projetos", "Comercial", "Produção", "Sócio"]
    created_roles = {}
    for role_name in roles_data:
        role = Papel.query.filter_by(nome_papel=role_name).first()
        if not role:
            role = Papel(nome_papel=role_name)
            db_instance.session.add(role)
        created_roles[role_name] = role
    
    # Seed Status Projeto
    project_statuses = ["Orçamento", "Planejamento", "Em Andamento", "Pausado", "Concluído", "Cancelado"]
    for status_name in project_statuses:
        if not StatusProjeto.query.filter_by(nome=status_name).first():
            db_instance.session.add(StatusProjeto(nome=status_name))

    # Seed Status Tarefa
    task_statuses = ["A Fazer", "Em Andamento", "Concluída", "Bloqueada", "Aguardando Aprovação"]
    for status_name in task_statuses:
        if not StatusTarefa.query.filter_by(nome=status_name).first():
            db_instance.session.add(StatusTarefa(nome=status_name))

    # Seed Status Conta (Financeiro)
    account_statuses = ["A Pagar", "Pago", "Vencido", "A Receber", "Recebido", "Parcialmente Pago/Recebido", "Cancelado"]
    for status_name in account_statuses:
        if not StatusConta.query.filter_by(nome=status_name).first():
            db_instance.session.add(StatusConta(nome=status_name))

    # Seed Status Orçamento
    quote_statuses = ["Em Elaboração", "Enviado", "Aprovado", "Rejeitado", "Em Negociação", "Convertido em Projeto", "Cancelado"]
    for status_name in quote_statuses:
        if not StatusOrcamento.query.filter_by(nome=status_name).first():
            db_instance.session.add(StatusOrcamento(nome=status_name))
    
    # Seed Centros de Custo
    cost_centers = ["Produção", "Criação e Desenvolvimento", "Administrativo", "Comercial"]
    for center_name in cost_centers:
        if not CentroCusto.query.filter_by(nome=center_name).first():
            db_instance.session.add(CentroCusto(nome=center_name))
    
    # Seed Usuário de Teste Administrador
    admin_email = "admin@cenart.br"
    if not Usuario.query.filter_by(email=admin_email).first():
        admin_user = Usuario(
            nome_completo="Admin CENART",
            email=admin_email,
            senha_hash=generate_password_hash("cenart123"), # Senha de teste, mudar em produção!
            papel_id=created_roles.get("Administrador").id if created_roles.get("Administrador") else None
        )
        db_instance.session.add(admin_user)

    try:
        db_instance.session.commit()
        print("Initial data seeded successfully!")
    except Exception as e:
        db_instance.session.rollback()
        print(f"Error seeding data: {e}")

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)

