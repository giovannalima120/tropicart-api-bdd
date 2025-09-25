from flask import Blueprint, request, jsonify
from services.empresa_services import *
from utils.mensagens_erro import ERROS

empresas_bp = Blueprint("empresas", __name__)

@empresas_bp.route("/empresas", methods=["GET"])
def listarEmpresas():
    return jsonify(listarEmpresas()), 200

@empresas_bp.route("/empresas/<int:id>", methods=["GET"])
def buscarEmpresa(id):
    empresaEncontrada, erro = buscarEmpresaPorId(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(empresaEncontrada), 200

@empresas_bp.route("/empresas", methods=["POST"])
def criar():
    dadosBody = request.json
    novaEmpresa, erro = criarEmpresa(dadosBody)

    if erro:
        errorInfo = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(novaEmpresa), 201

@empresas_bp.route("/empresas/<int:id>", methods=["PUT"])
def atualizar(id):
    empresa, erro = editarEmpresa(id, request.json)

    if erro: 
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(empresa), 200

@empresas_bp.route("/empresas/<int:id>", methods=["DELETE"])
def deletar(id):
    sucesso, erro = deletarEmpresa(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return "", 204


