from .receita import Receita
import pickle
class Carteira:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(transacao)

    def saldo(self):
        return sum(t.get_valor() if isinstance(t, Receita) else -t.get_valor() for t in self.transacoes)

    def salvar(self, caminho):
        with open(caminho, 'wb') as f:
            pickle.dump(self.transacoes, f)

    def carregar(self, caminho):
        try:
            with open(caminho, 'rb') as f:
                self.transacoes = pickle.load(f)
        except FileNotFoundError:
            self.transacoes = []
