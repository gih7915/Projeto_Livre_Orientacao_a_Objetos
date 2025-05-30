class Transacao:
    def __init__(self, valor, data, categoria, descricao):
        self._valor = valor
        self._data = data
        self._categoria = categoria
        self._descricao = descricao

    def get_valor(self):
        return self._valor

    def get_info(self):
        return f"{self._data} - {self._descricao} - R${self._valor:.2f}"
