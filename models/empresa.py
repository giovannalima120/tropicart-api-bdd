from models.usuario import Usuario

class Empresa(Usuario):
    def __init__ (self, id, username, nome, email, senha):
        super().__init__(id, username, nome, email, senha, "Empresa")
