from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario


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
    return UsuarioDAO.select_user_by_username(dados["username"]), None

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

def editarUsuario(id, novosDados):
    usuarioEncontrado, erro = buscarUserPorId(id)

    if erro:
        return None, erro
    
    if "username" in novosDados:
        outro = UsuarioDAO.select_user_by_username(novosDados["username"])
        if outro and outro["id"] != id:
            return None, "USERNAME_DUPLICADO"
  
    if "email" in novosDados:
        todos = UsuarioDAO.get_all_users()
        if any(u["email"] == novosDados["email"] and u["id"] != id for u in todos):
            return None, "EMAIL_DUPLICADO"
        
    usuarioAtualizado = UsuarioDAO.update_user_by_id(id, novosDados)
    return usuarioAtualizado, None

    
def deletarUsuario(id):
    usuario, erro = buscarUserPorId(id)
    if erro:
        return False, erro
    
    UsuarioDAO.delete_user_by_id(id)
    return True, None