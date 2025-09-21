class Usuario:
    def __init__ (self, id, username, nome, email, senha, categoria):
        self.id = id
        self.username = username
        self.nome = nome
        self.email = email
        self.senha = senha
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "nome": self.nome,
            "email": self.email,
            "categoria": self.categoria
        }
