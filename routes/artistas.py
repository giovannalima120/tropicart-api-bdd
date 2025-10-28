from flask import Blueprint, request, jsonify
from services.artista_services import *
from utils.mensagens_erro import ERROS

artistas_bp = Blueprint("artistas", __name__)

@artistas_bp.route("/", methods=["GET"])
def listarArtistas():
    artistas = ArtistaDAO.get_all_artistas()
    return jsonify(artistas), 200

@artistas_bp.route("/<int:id>", methods=["GET"])
def buscarArtista(id):
    artistaEncontrado, erro = buscarArtistaPorId(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(artistaEncontrado), 200

@artistas_bp.route("/", methods=["POST"])
def criar():
    dadosBody = request.json
    usuario_id = dadosBody.get("usuario_id")
    area = dadosBody.get("area")

    novoArtista, erro = ArtistaDAO.insert_artista(usuario_id, area)

    if erro:
        errorInfo = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(novoArtista), 201

@artistas_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    artista, erro = editarArtista(id, request.json)

    if erro: 
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return jsonify(artista), 200

@artistas_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    sucesso, erro = deletarArtista(id)

    if erro:
        errorInfo = ERROS[erro]
        return jsonify({"mensagem": errorInfo["mensagem"]}), errorInfo["status"]
    return "", 204


