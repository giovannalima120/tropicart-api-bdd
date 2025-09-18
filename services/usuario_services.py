from models.usuario import Usuario

usuarios = []

idUsuario = 0

def gerarId():
    global idUsuario
    idUsuario += 1
    return idUsuario

def criarUsuario(dados):
    for u in usuarios:
        if u.email == dados["email"]:
            return None, "EMAIL_DUPLICADO"
