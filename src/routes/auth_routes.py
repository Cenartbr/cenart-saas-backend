from flask import Blueprint, request, jsonify
from src.models.usuario import Usuario
from werkzeug.security import check_password_hash
# Para JWT, precisaremos de Flask-JWT-Extended ou similar. Adicionaremos depois se necessário.
# from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Email e senha são obrigatórios"}), 400

    user = Usuario.query.filter_by(email=data.get("email")).first()

    if not user or not user.check_password(data.get("password")):
        return jsonify({"message": "Credenciais inválidas"}), 401

    # Simples resposta por enquanto. Em uma implementação real, geraríamos um token JWT.
    # access_token = create_access_token(identity=user.id) # Exemplo com Flask-JWT-Extended
    return jsonify({
        "message": "Login bem-sucedido!",
        "user": {
            "id": user.id,
            "nome": user.nome_completo,
            "email": user.email,
            "papel": user.papel.nome_papel if user.papel else "N/A" # Assumindo que a relação 'papel' existe e tem 'nome_papel'
        },
        # "access_token": access_token # Exemplo com Flask-JWT-Extended
        "token": f"fake-jwt-token-for-{user.id}" # Token simulado para desenvolvimento
    }), 200

# Outras rotas de autenticação (registro, logout, refresh token) podem ser adicionadas aqui.

