class Despesa:
    def __init__(self, valor, data, categoria, descricao):
        self._valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    def get_valor(self):
        return self._valor
