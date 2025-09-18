class Vaga:
    def __init__ (self, id, titulo, salario, localizacao, requisito, descricao):
        self.id = id
        self.titulo = titulo
        self.salario = salario
        self.localizacao = localizacao
        self.requisito = requisito
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "salario": self.salario,
            "localizacao": self.localizacao,
            "requisito": self.requisito,
            "descricao": self.descricao
        }
       
