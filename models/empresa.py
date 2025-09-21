from models.usuario import Usuario

class Empresa(Usuario):
    def __init__ (self, username, nome, email, senha, categoria):
        super().__init__(id, username, nome, email, senha, categoria)

    def to_dict(self):
        dados = super().to_dict()
        return dados