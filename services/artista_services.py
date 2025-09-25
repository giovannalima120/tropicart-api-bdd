from dao.artista_dao import ArtistaDAO
from dao.usuario_dao import UsuarioDAO


def criarArtista(dados):


    if ArtistaDAO.select_artista_by_username(dados["username"]):
        return None, "USERNAME_DUPLICADO"
    
    todos = ArtistaDAO.get_all_artistas()
    if any(u["email"] == dados["email"] for u in todos):
        return None, "EMAIL_DUPLICADO"

    
    UsuarioDAO.insert_user(
        dados["username"],
        dados["nome"],
        dados["email"],
        dados["senha"],
        "Artista"
    )

    usuario = UsuarioDAO.select_user_by_username(dados["username"])
    usuario_id = usuario["id"]

    ArtistaDAO.insert_artista(usuario_id, dados["area"])
    
    novoArtista = ArtistaDAO.select_artista_by_id(usuario_id)
    return novoArtista, None

def listarArtistas():
    return ArtistaDAO.get_all_artistas()

def buscarArtistaPorId(id):
    artista = ArtistaDAO.select_artista_by_id(id)

    if not artista:
        return None, "ARTISTA_NAO_ENCONTRADO"
    
    return artista, None

def buscarArtistaPorUsername(username):
    artista = ArtistaDAO.select_artista_by_username(username)

    if not artista:
        return None, "ARTISTA_NAO_ENCONTRADO"
    
    return artista, None

def editarArtista(id, novosDados):
    artistaEncontrado, erro = buscarArtistaPorId(id)

    if erro:
        return None, "ARTISTA_NAO_ENCONTRADO"
    
    if "username" in novosDados:
        outro = ArtistaDAO.select_artista_by_username(novosDados["username"])
        if outro and outro["id"] != id:
            return None, "USERNAME_DUPLICADO"
  
    if "email" in novosDados:
        todos = ArtistaDAO.get_all_artistas()
        if any(u["email"] == novosDados["email"] and u["id"] != id for u in todos):
            return None, "EMAIL_DUPLICADO"
        
    artistaAtual = artistaEncontrado
    username = novosDados.get("username", artistaAtual["username"])
    nome = novosDados.get("nome", artistaAtual["nome"])
    email = novosDados.get("email", artistaAtual["email"])
    senha = novosDados.get("senha", artistaAtual["senha"])
    area = novosDados.get("area", artistaAtual["area"])
    
    ArtistaDAO.update_artista_by_id(username, nome, email, senha, area)
    artistaAtualizado = ArtistaDAO.select_artista_by_id(id)
    return artistaAtualizado, None

    
def deletarArtista(id):
    artista, erro = buscarArtistaPorId(id)
    if erro:
        return False, "ARTISTA_NAO_ENCONTRADO"
    
    ArtistaDAO.delete_artista_by_id(id)
    return True, None