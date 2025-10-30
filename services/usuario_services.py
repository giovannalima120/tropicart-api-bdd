from dao.usuario_dao import UsuarioDAO
from dao.empresa_dao import EmpresaDAO
from dao.artista_dao import ArtistaDAO


def criarUsuario(dados):


    if UsuarioDAO.select_user_by_username(dados["username"]):
        return None, "USERNAME_DUPLICADO"
    
    todos = UsuarioDAO.get_all_users()
    if any(u["email"] == dados["email"] for u in todos):
        return None, "EMAIL_DUPLICADO"

    
    UsuarioDAO.insert_user(
        dados["username"],
        dados["nome"],
        dados["email"],
        dados["senha"],
        dados["categoria"]
    )
    usuario = UsuarioDAO.select_user_by_username(dados["username"])

    if usuario["categoria"].lower() == "artista":
        area = dados.get("area", "Não informado")
        ArtistaDAO.insert_artista(usuario["id"], area)
    elif usuario["categoria"].lower() == "empresa":
        EmpresaDAO.insert_empresa(usuario["id"])

    return usuario, None

def listarUsuarios():
    return UsuarioDAO.get_all_users()

def buscarUserPorId(id):
    user = UsuarioDAO.select_user_by_id(id)

    if not user:
        return None, "USUARIO_NAO_ENCONTRADO"
    
    return user, None

def buscarUserPorUsername(username):
    user = UsuarioDAO.select_user_by_username(username)

    if not user:
        return None, "USUARIO_NAO_ENCONTRADO"
    
    return user, None

def buscarUserPorEmail(email):
    user = UsuarioDAO.select_user_by_email(email)

    if not user:
        return None, "USUARIO_NAO_ENCONTRADO"
    
    return user, None

def editarUsuario(id, novosDados):
    usuarioEncontrado, erro = buscarUserPorId(id)

    if erro:
        return None, "USUARIO_NAO_ENCONTRADO"
    
    if "username" in novosDados:
        outro = UsuarioDAO.select_user_by_username(novosDados["username"])
        if outro and outro["id"] != id:
            return None, "USERNAME_DUPLICADO"
  
    if "email" in novosDados:
        todos = UsuarioDAO.get_all_users()
        if any(u["email"] == novosDados["email"] and u["id"] != id for u in todos):
            return None, "EMAIL_DUPLICADO"
    
    username = novosDados.get("username", usuarioEncontrado["username"])
    nome = novosDados.get("nome", usuarioEncontrado["nome"])
    email = novosDados.get("email", usuarioEncontrado["email"])
    senha = novosDados.get("senha", usuarioEncontrado["senha"])

    print(f"Atualizando usuário: username={username}, nome={nome}, email={email}, senha={senha}, id={id}")
    UsuarioDAO.update_user_by_id(username, nome, email, senha, id)

    usuarioAtualizado = UsuarioDAO.select_user_by_id(id)
    return usuarioAtualizado, None

    
def deletarUsuario(id):
    usuario, erro = buscarUserPorId(id)
    if erro:
        return False, "USUARIO_NAO_ENCONTRADO"
    
    UsuarioDAO.delete_user_by_id(id)
    return True, None