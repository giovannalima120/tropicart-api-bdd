from flask import Blueprint, request, jsonify
from services.usuario_services import *
from utils.mensagens_erro import ERROS

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def listarUsuarios():
    return jsonify(listarUsuarios()), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscarUsuario(id):
    usuarioEncontrado, erro = buscarUserPorId(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(usuarioEncontrado), 200

@usuarios_bp.route("/usuarios", methods=["POST"])
def criar():
    dadosBody = request.json
    novoUsuario, erro = criarUsuario(dadosBody)

    if erro:
        errorInfo = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(novoUsuario), 201

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar(id):
    usuario, erro = editarUsuario(id, request.json)

    if erro: 
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(usuario), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar(id):
    sucesso, erro = deletarUsuario(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return "", 204


