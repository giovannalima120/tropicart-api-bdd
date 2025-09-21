from models.usuario import Usuario

usuarios = []

idUsuario = 0

def gerarId():
    global idUsuario
    idUsuario += 1
    return idUsuario

def criarUsuario(dados):

    for u in usuarios:
        if u.username == dados["username"]:
            return None, "USERNAME_DUPLICADO"
        
    for u in usuarios:
        if u.email == dados["email"]:
            return None, "EMAIL_DUPLICADO"
    
        novoUsuario = Usuario(gerarId(), dados)
        usuarios.append(novoUsuario)
        return novoUsuario, None

def listarUsuarios():
    lista = [u.to_dict() for u in usuarios]
    return lista

def buscarUserPorId(id):
    for u in usuarios:
        if u.id == id:
            return u, None
    return None, "USUARIO_NAO_ENCONTRADO"

def buscarUserPorUsername(username):
    for u in usuarios:
        if u.username == username:
            return u, None
    return None, "USUARIO_NAO_ENCONTRADO"

def editarUsuario(id, novosDados):
    usuarioEncontrado, erro = buscarUserPorId(id)

    if erro:
        return None, erro
    
    novoEmail = novosDados.get("email")
    novoUsername = novosDados.get("username")

    if(novoUsername):
        for u in usuarios:
            if u.username == novosDados["username"]:
                return None, "USERNAME_DUPLICADO"
            
    if(novoEmail):
        for u in usuarios:
            if u.email == novosDados["email"]:
                return None, "EMAIL_DUPLICADO"
    
        usuarioEncontrado.username = novosDados.get("username", usuarioEncontrado.username)
        usuarioEncontrado.nome = novosDados.get("nome", usuarioEncontrado.nome)
        usuarioEncontrado.email = novosDados.get("email", usuarioEncontrado.email)
        usuarioEncontrado.senha = novosDados.get("senha", usuarioEncontrado.senha)
        usuarioEncontrado.categoria = novosDados.get("categoria", usuarioEncontrado.categoria)
        return usuarioEncontrado, None
    
def deletarUsuario(id):
    global usuarios
    usuarioEncontrado, erro = buscarUserPorId(id)

    if erro:
        return False, erro
    
    usuarios.remove(usuarioEncontrado)
    return True, None