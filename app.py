from flask import Flask, render_template, request, redirect, url_for
categorias = ["Comida", "Saúde", "Transporte", "Lazer"]  # categorias fixas no momento
from package.receita import Receita
from package.despesa import Despesa
from package.categoria import Categoria
from package.carteira import Carteira

app = Flask(__name__)
carteira = Carteira()
carteira.carregar("data/dados.pkl")

from collections import defaultdict
import calendar
from datetime import datetime

@app.route('/')
def index():
    transacoes_por_mes = defaultdict(list)

    for i, t in enumerate(carteira.transacoes):
        data = datetime.strptime(t.data, "%Y-%m-%d")
        nome_mes = f"{calendar.month_name[data.month]} {data.year}"
        transacoes_por_mes[nome_mes].append((i, t))

    return render_template('index.html',
                           transacoes_por_mes=transacoes_por_mes,
                           saldo=carteira.saldo(),
                           categorias=categorias)


@app.route('/nova', methods=['POST'])
def nova_transacao():
    tipo = request.form['tipo']
    valor = float(request.form['valor'])
    data = request.form['data']
    categoria = request.form['categoria']
    descricao = request.form['descricao']

    if categoria == "nova":
        nova_categoria = request.form['nova_categoria'].strip()
        if nova_categoria and nova_categoria not in categorias:
            categorias.append(nova_categoria)
            categoria = nova_categoria

    if tipo == 'receita':
        transacao = Receita(valor, data, categoria, descricao)
    else:
        transacao = Despesa(valor, data, categoria, descricao)

    carteira.adicionar(transacao)

    return redirect(url_for('index'))


@app.route('/excluir/<int:index>', methods=['POST'])
def excluir_transacao(index):
    try:
        carteira.transacoes.pop(index)
        carteira.salvar("data/dados.pkl")
    except IndexError:
        pass
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)