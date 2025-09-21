from models.usuario import Usuario

class Artista(Usuario):
    def __init__ (self, area, id, username, nome, email, senha, categoria):
        super().__init__(id, username, nome, email, senha, categoria)
        self.area = area
        self.vagasInscritas = []


    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "area": self.area,
            "vagasInscritas": self.vagasInscritas
        })
        return dados