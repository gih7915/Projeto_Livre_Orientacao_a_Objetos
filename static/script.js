// Array para armazenar transações na memória
const transacoes = [];

const form = document.getElementById('form-transacao');
const tabelaCorpo = document.querySelector('#tabela-transacoes tbody');
const saldoDiv = document.getElementById('saldo');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const tipo = document.getElementById('tipo').value;
  const descricao = document.getElementById('descricao').value.trim();
  const valor = parseFloat(document.getElementById('valor').value);

  if (!descricao || isNaN(valor) || valor <= 0 || !tipo) {
    alert('Por favor, preencha todos os campos corretamente.');
    return;
  }

  // Cria a transação e adiciona no array
  const transacao = { tipo, descricao, valor };
  transacoes.push(transacao);

  // Atualiza a tabela e o saldo na página
  atualizarTabela();
  atualizarSaldo();

  // Limpa o formulário
  form.reset();
});

function atualizarTabela() {
  tabelaCorpo.innerHTML = ''; // limpa tabela

  transacoes.forEach(t => {
    const tr = document.createElement('tr');

    const tdDesc = document.createElement('td');
    tdDesc.textContent = t.descricao;
    tr.appendChild(tdDesc);

    const tdValor = document.createElement('td');
    tdValor.textContent = `R$ ${t.valor.toFixed(2)}`;
    tr.appendChild(tdValor);

    const tdTipo = document.createElement('td');
    tdTipo.textContent = t.tipo;
    tr.appendChild(tdTipo);

    tabelaCorpo.appendChild(tr);
  });
}

function atualizarSaldo() {
  let saldo = 0;
  transacoes.forEach(t => {
    if (t.tipo === 'receita') {
      saldo += t.valor;
    } else if (t.tipo === 'despesa') {
      saldo -= t.valor;
    }
  });

  saldoDiv.textContent = `Saldo: R$ ${saldo.toFixed(2)}`;
}
