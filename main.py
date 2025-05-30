from package.receita import Receita
from package.despesa import Despesa
from package.categoria import Categoria
from package.carteira import Carteira

carteira = Carteira()
carteira.carregar("data/dados.pkl")

# Exemplo de uso
cat_salario = Categoria("Salário")
cat_compras = Categoria("Compras")

r1 = Receita(3000, "2025-05-01", cat_salario, "Salário Maio")
d1 = Despesa(200, "2025-05-03", cat_compras, "Mercado")

carteira.adicionar(r1)
carteira.adicionar(d1)

print("Transações:")
for t in carteira.transacoes:
    print(t.get_info())

print(f"Saldo atual: R${carteira.saldo():.2f}")

carteira.salvar("data/dados.pkl")