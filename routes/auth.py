from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from dao.usuario_dao import get_db_connection
from models.usuario import Usuario
from services.usuario_services import criar_usuario, buscar_usuario_por_email

auth_bp = Blueprint('auth', __name__)
blacklist = set()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('senha'):
        return jsonify({"error": "Dados incompletos"}), 400
    
    existing_user = buscar_usuario_por_email(data['email'])
    if existing_user:
        return jsonify({"error": "Email já cadastrado"}), 409
    
    hashed_password = generate_password_hash(data['senha'])
    usuario = Usuario(
        nome=data.get('nome'),
        email=data['email'],
        senha=hashed_password,
        tipo=data.get('tipo', 'comum')
    )
    
    criar_usuario(usuario)
    return jsonify({"message": "Usuário registrado com sucesso"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('senha'):
        return jsonify({"error": "Dados incompletos"}), 400
    
    usuario = buscar_usuario_por_email(data['email'])
    if not usuario or not check_password_hash(usuario.senha, data['senha']):
        return jsonify({"error": "Credenciais inválidas"}), 401
    
    access_token = create_access_token(identity=usuario.id)
    return jsonify({"token": access_token}), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({"message": "Logout realizado com sucesso"}), 200