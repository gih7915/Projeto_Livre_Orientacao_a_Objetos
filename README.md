# Projeto_Livre_Orientacao_a_Objetos
# 💰 Controle Financeiro da Gih

Este projeto é um sistema de controle financeiro pessoal, desenvolvido para a disciplina de **Orientação a Objetos (01/2025)** na **Faculdade UnB Gama**. Ele permite gerenciar receitas e despesas com base em categorias, datas e descrições, exibindo o saldo total atualizado.

## 🚀 Funcionalidades

- ✅ Cadastro de receitas e despesas
- ✅ Classificação por categoria e data
- ✅ Visualização das transações organizadas por mês
- ✅ Exclusão de transações
- ✅ Cálculo automático do saldo final
- ✅ Persistência de dados (serialização com `pickle`)
- ✅ Interface web com Flask

---

## 🧠 Casos de Uso

### 📌 Caso 1: Adicionar Receita ou Despesa
- **Ator**: Usuário
- **Descrição**: O usuário insere uma nova transação (receita ou despesa) com valor, data, categoria e descrição.

### 📌 Caso 2: Visualizar Transações
- **Ator**: Usuário
- **Descrição**: O sistema exibe as transações agrupadas por mês, com tipo, valor e categoria.

### 📌 Caso 3: Excluir Transação
- **Ator**: Usuário
- **Descrição**: O usuário pode excluir uma transação específica clicando em “Excluir”.

---

## 🧱 Estrutura de Classes

package/
│
├── carteira.py      # Classe controladora principal (Carteira)
├── categoria.py     # Classe para lidar com categorias
├── receita.py       # Subclasse de Transação para receitas
├── despesa.py       # Subclasse de Transação para despesas
├── mixin.py         # Classe mixin (ex: salvar em arquivo ou exibir dados)

## 🔄 Paradigmas e Padrões Usados
-✅ Herança: Receita e Despesa herdam de uma classe base Transacao

-✅ Polimorfismo: Métodos como get_valor() são sobrescritos ou usados de forma uniforme

-✅ Composição forte: Carteira contém várias Transacao

-✅ Associação fraca: Transacao utiliza uma instância de Categoria

-✅ Mixin: Classe auxiliar para salvar ou exportar dados

## 💾 Serialização
Os dados das transações são salvos e carregados automaticamente no arquivo data/dados.pkl utilizando o módulo pickle, garantindo que o histórico do usuário seja preservado.

## 🖥️ Interface
Apesar do requisito solicitar interface desktop, esta versão utiliza o Flask para criar uma interface web simples e responsiva, que pode ser adaptada para desktop futuramente com PyQt5 ou Tkinter.
