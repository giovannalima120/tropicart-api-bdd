class Usuario:
    def __init__ (self, id, nome, email, senha, categoria):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "categoria": self.categoria
        }
