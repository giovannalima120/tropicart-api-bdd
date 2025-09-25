from flask import Blueprint, request, jsonify
from services.artista_services import *
from utils.mensagens_erro import ERROS

artistas_bp = Blueprint("artistas", __name__)

@artistas_bp.route("/artistas", methods=["GET"])
def listarArtistas():
    return jsonify(listarArtistas()), 200

@artistas_bp.route("/artistas/<int:id>", methods=["GET"])
def buscarArtista(id):
    artistaEncontrado, erro = buscarArtistaPorId(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(artistaEncontrado), 200

@artistas_bp.route("/artistas", methods=["POST"])
def criar():
    dadosBody = request.json
    novoArtista, erro = criarArtista(dadosBody)

    if erro:
        errorInfo = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(novoArtista), 201

@artistas_bp.route("/artistas/<int:id>", methods=["PUT"])
def atualizar(id):
    artista, erro = editarArtista(id, request.json)

    if erro: 
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(artista), 200

@artistas_bp.route("/artistas/<int:id>", methods=["DELETE"])
def deletar(id):
    sucesso, erro = deletarArtista(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return "", 204


