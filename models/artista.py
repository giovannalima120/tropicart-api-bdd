from models.usuario import Usuario

class Artista(Usuario):
    def __init__ (self, area, id, username, nome, email, senha, categoria):
        super().__init__(id, username, nome, email, senha, categoria)
        self.area = area
        self.vagasInscritas = []