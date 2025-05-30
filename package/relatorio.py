class Relatorio:
    def __init__(self, transacoes):
        self.transacoes = transacoes

    def por_categoria(self, nome):
        return [t for t in self.transacoes if t._categoria.nome == nome]
