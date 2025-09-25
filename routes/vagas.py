from flask import Blueprint, request, jsonify
from services.vagas_services import *
from utils.mensagens_erro import ERROS

vagas_bp = Blueprint("vagas", __name__)

@vagas_bp.route("/vagas_bp", methods=["GET"])
def listarVagas():
    return jsonify(listarVagas()), 200

@vagas_bp.route("/<int:id>", methods=["GET"])
def buscarVaga(id):
    vagaEncontrada, erro = buscarVagaPorId(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(vagaEncontrada), 200

@vagas_bp.route("/<int:empresa_id>", methods=["GET"])
def buscarVagaPorEmpresa(empresa_id):
    vagaEncontrada, erro = buscarVagaPorEmpresa(empresa_id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(vagaEncontrada), 200

@vagas_bp.route("/<titulo>", methods=["GET"])
def buscarVagaPorTitulo(titulo):
    vagaEncontrada, erro = buscarVagaPorTitulo(titulo)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(vagaEncontrada), 200

@vagas_bp.route("/vagas", methods=["POST"])
def criar():
    dadosBody = request.json
    novaVaga, erro = criarVaga(dadosBody)

    if erro:
        errorInfo = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(novaVaga), 201

@vagas_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    usuario, erro = editarVaga(id, request.json)

    if erro: 
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(usuario), 200

@vagas_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    sucesso, erro = deletarVaga(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return "", 204


