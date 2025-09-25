from dao.empresa_dao import EmpresaDAO
from dao.usuario_dao import UsuarioDAO


def criarEmpresa(dados):


    if EmpresaDAO.select_empresa_by_username(dados["username"]):
        return None, "USERNAME_DUPLICADO"
    
    todos = EmpresaDAO.get_all_empresas()
    if any(u["email"] == dados["email"] for u in todos):
        return None, "EMAIL_DUPLICADO"

    
    UsuarioDAO.insert_user(
        dados["username"],
        dados["nome"],
        dados["email"],
        dados["senha"],
        "Empresa"
    )

    usuario = UsuarioDAO.select_user_by_username(dados["username"])
    usuario_id = usuario["id"]
    empresaNova = EmpresaDAO.select_empresa_by_id(usuario_id)
    return empresaNova, None

def listarEmpresas():
    return EmpresaDAO.get_all_empresas()

def buscarEmpresaPorId(id):
    empresa = EmpresaDAO.select_empresa_by_id(id)

    if not empresa:
        return None, "EMPRESA_NAO_ENCONTRADA"
    
    return empresa, None

def buscarEmpresaPorUsername(username):
    empresa = EmpresaDAO.select_empresa_by_username(username)

    if not empresa:
        return None, "EMPRESA_NAO_ENCONTRADA"
    
    return empresa, None

def editarEmpresa(id, novosDados):
    empresaEncontrada, erro = buscarEmpresaPorId(id)

    if erro:
        return None, "EMPRESA_NAO_ENCONTRADA"
    
    if "username" in novosDados:
        outro = EmpresaDAO.select_empresa_by_username(novosDados["username"])
        if outro and outro["id"] != id:
            return None, "USERNAME_DUPLICADO"
  
    if "email" in novosDados:
        todos = EmpresaDAO.get_all_empresas()
        if any(u["email"] == novosDados["email"] and u["id"] != id for u in todos):
            return None, "EMAIL_DUPLICADO"
        
    empresaAtual = empresaEncontrada
    username = novosDados.get("username", empresaAtual["username"])
    nome = novosDados.get("nome", empresaAtual["nome"])
    email = novosDados.get("email", empresaAtual["email"])
    senha = novosDados.get("senha", empresaAtual["senha"])
    
    EmpresaDAO.update_empresa_by_id(username, nome, email, senha, id)
    empresaAtualizada = EmpresaDAO.select_empresa_by_id(id)
    return empresaAtualizada, None

    
def deletarEmpresa(id):
    empresa, erro = buscarEmpresaPorId(id)
    if erro:
        return False, "EMPRESA_NAO_ENCONTRADA"
    
    EmpresaDAO.delete_empresa_by_id(id)
    return True, None