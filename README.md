# 💰 Controle Financeiro da Gih

Projeto desenvolvido para a disciplina **Orientação a Objetos** (01/2025)  
Faculdade UnB Gama — Prof. Henrique Moura

---

## Acesse o link do projeto
https://projeto-livre-orientacao-a-objetos-3.onrender.com/

---

## 📋 Definição do Problema

Este projeto tem como objetivo criar um sistema para controle financeiro pessoal, que permita ao usuário cadastrar receitas e despesas, visualizar o saldo atual e organizar as transações por mês e categoria.

---

## ✅ Casos de Uso

### 1. Adicionar Transação
- **Ator:** Usuário
- **Descrição:** O usuário cadastra uma nova transação (receita ou despesa), informando valor, data, categoria e descrição.
- **Fluxo:**
  1. O usuário abre o formulário de nova transação.
  2. Preenche os dados solicitados.
  3. Envia o formulário.
  4. O sistema salva a transação e atualiza o saldo.

### 2. Excluir Transação
- **Ator:** Usuário
- **Descrição:** O usuário pode excluir uma transação previamente cadastrada.
- **Fluxo:**
  1. O usuário localiza a transação na lista.
  2. Clica no botão “Excluir”.
  3. O sistema remove a transação e atualiza o saldo.

### 3. Visualizar Transações
- **Ator:** Usuário
- **Descrição:** O sistema apresenta as transações agrupadas por mês, exibindo saldo e categorias.

---

## 🧠 Modelagem Orientada a Objetos

- **Herança:**  
  `Receita` e `Despesa` herdam da classe base `Transacao`.
  
- **Polimorfismo:**  
  Métodos como `get_valor()` e `get_info()` têm implementações específicas em `Receita` e `Despesa`.
  
- **Composição forte:**  
  A classe `Carteira` contém a lista de transações, que não existem fora dela.
  
- **Associação fraca:**  
  Cada `Transacao` está associada a uma `Categoria`, que pode ser compartilhada entre transações.

---

## 📋Diagrama de Classes

## 📘 Diagrama de Classes

Diagrama de classes representando a modelagem do sistema de controle financeiro:

```text
+---------------------+
|     Categoria       |
+---------------------+
| - nome: str         |
+---------------------+
| +__init__()         |
| +get_nome()         |
```

```text
+---------------------+
|      Receita        |
+---------------------+
| - valor: float      |
| - data: date        |
| - categoria: str    |
+---------------------+
| +__init__()         |
| +get_valor()        |
| +get_data()         |
| +get_categoria()    |
```

```text
+---------------------+
|      Despesa        |
+---------------------+
| - valor: float      |
| - data: date        |
| - categoria: str    |
+---------------------+
| +__init__()         |
| +get_valor()        |
| +get_data()         |
| +get_categoria()    |
```

```text
+---------------------+
|      Carteira       |
+---------------------+
| - receitas: list    |
| - despesas: list    |
+---------------------+
| +__init__()         |
| +adicionar_receita()|
| +adicionar_despesa()|
| +saldo_total()      |
```

```text
+---------------------+
|     main.py         |
+---------------------+
| (Controlador Flask) |
+---------------------+
| +rotas de interface |
```

### Relações:
- `Carteira` possui `Receita` e `Despesa`
- `Receita` e `Despesa` têm uma `Categoria`


---

## 🗂 Estrutura do Projeto

```text
controle-financeiro/
├── main.py                  # Lógica principal com Flask
├── README.md                # Este arquivo
├── data/
│   └── dados.pkl            # Dados serializados
├── static/
│   └── styles.css           # Estilo da página
├── templates/
│   └── index.html           # Página principal
└── package/
    ├── carteira.py          # Classe Carteira
    ├── categoria.py         # Classe Categoria
    ├── receita.py           # Classe Receita
    └── despesa.py           # Classe Despesa
```


---

## 💾 Serialização

O sistema utiliza o módulo `pickle` para serializar e desserializar os objetos da carteira, garantindo persistência dos dados entre execuções.

---

## 🖥 Interface Gráfica

Desenvolvida com Flask, a interface é simples e intuitiva, apresentando as transações agrupadas por mês e categoria, com formulários para inclusão e exclusão de transações.

---

## 📬 Contato

- Email: giovana79155@gmail.com  

---

**Projeto desenvolvido por Giovana — 2025**
