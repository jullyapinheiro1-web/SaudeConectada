# SaúdeConectada

## 1. Nome do Projeto

### SaúdeConectada

---

## 2. Descrição do Projeto

O SaúdeConectada é um sistema web desenvolvido com o objetivo de facilitar
o acesso da população a informações sobre vacinação.

O sistema busca solucionar a dificuldade de acesso a informações claras
sobre vacinas, campanhas e locais de vacinação, especialmente para pessoas
que vivem em regiões mais distantes.

A plataforma disponibilizará informações sobre vacinas, campanhas de
vacinação e locais disponíveis para atendimento, além de uma tela inicial
e uma tela de login para facilitar o acesso e a navegação dos usuários
pelo sistema.

---

## 3. Tecnologias Utilizadas

As tecnologias utilizadas no desenvolvimento do projeto são:

- Python
- Django
- HTML
- CSS
- SQLite
- Bootstrap Icons

---

## 4. Equipe

| Integrante | Responsabilidade |

| Fabrício Lemos | Desenvolvimento da tela de locais de vacinação e cadastro de locais;
| Thayla Vitória| Desenvolvimento da tela de campanhas e cadastro de campanhas;
| Jullya Pinheiro | Desenvolvimento da tela de vacinas e cadastro de vacinas;
| Suellen Vitória | Desenvolvimento da tela inicial e tela de login.

---

## 5. Apps Django

### principal

O projeto possui o aplicativo Django `principal`, responsável por reunir
as principais funcionalidades do sistema SaúdeConectada.

O app `principal` é responsável pelas funcionalidades de:

- Tela inicial;
- Tela de login;
- Vacinas;
- Campanhas;
- Locais de vacinação;
- Formulários;
- Views;
- Rotas das funcionalidades;
- Integração com o Django Admin.

As funcionalidades do app serão desenvolvidas pelos integrantes do grupo
de acordo com as responsabilidades definidas pela equipe.

A pasta `templates` não é um App Django. Ela é utilizada para armazenar
os arquivos HTML das páginas do sistema.

---

## 6. Models e Views

### Model Vacina

O Model `Vacina` é responsável por armazenar as informações das vacinas
cadastradas no sistema.

Principais informações:

- Nome da vacina;
- Fabricante;
- Número do lote;
- Tipo de dose;
- Descrição.

**Responsável:** Jullya Pinheiro.

**Views relacionadas:**

- Listagem de vacinas;
- Visualização dos detalhes da vacina;
- Cadastro de vacinas;
- Edição de vacinas;
- Exclusão de vacinas.

---

### Model Campanha

O Model `Campanha` é responsável por armazenar as informações das campanhas
de vacinação.

Principais informações:

- Nome;
- Descrição;
- Data de início;
- Data de fim;
- Vacinas relacionadas;
- Locais de vacinação relacionados.

**Responsável:** Thayla.

**Views relacionadas:**

- Visualização de campanhas;
- Cadastro de campanhas;
- Edição de campanhas;
- Exclusão de campanhas.

---

### Model LocalVacinacao

O Model `LocalVacinacao` é responsável por armazenar as informações dos
locais disponíveis para vacinação.

Principais informações:

- Nome;
- Endereço;
- Cidade.

**Responsável:** Fabrício Lemos.

**Views relacionadas:**

- Visualização de locais de vacinação;
- Cadastro de locais;
- Edição de locais;
- Exclusão de locais.

---

### Tela Inicial

A tela inicial será responsável por apresentar o sistema ao usuário e
facilitar o acesso às principais funcionalidades do SaúdeConectada.

**Responsável:** Suellen Vitória.

**View relacionada:**

- `home`

---

### Tela de Login

A tela de login será responsável pelo acesso dos usuários ao sistema.

**Responsável:** Suellen Vitória.

**Views relacionadas:**

- Funcionalidades de autenticação;
- Login e acesso ao sistema.

---

## 7. Arquivos e Responsabilidades

### Fabrício Lemos — Locais de Vacinação

**Responsabilidades:**

- Desenvolver a tela de locais de vacinação;
- Desenvolver o cadastro de locais;
- Desenvolver as funcionalidades relacionadas aos locais de vacinação;
- Desenvolver ou modificar os arquivos necessários para essa funcionalidade.

**Principais arquivos:**

- `principal/models.py`
- `principal/views.py`
- `principal/forms.py`
- `principal/urls.py`
- `templates/principal/locais.html`

---

### Thayla Vitória — Campanhas

**Responsabilidades:**

- Desenvolver a tela de campanhas;
- Desenvolver o cadastro de campanhas;
- Desenvolver as funcionalidades relacionadas às campanhas;
- Desenvolver ou modificar os arquivos necessários para essa funcionalidade.

**Principais arquivos:**

- `principal/models.py`
- `principal/views.py`
- `principal/forms.py`
- `principal/urls.py`
- `templates/principal/campanhas.html`

---

### Jullya Pinheiro — Vacinas

**Responsabilidades:**

- Desenvolver a tela de vacinas;
- Desenvolver o cadastro de vacinas;
- Desenvolver a listagem de vacinas;
- Desenvolver a visualização dos detalhes das vacinas;
- Desenvolver a edição de vacinas;
- Desenvolver a exclusão de vacinas;
- Desenvolver ou modificar os arquivos necessários para essas funcionalidades.

**Principais arquivos:**

- `principal/models.py`
- `principal/views.py`
- `principal/forms.py`
- `principal/urls.py`
- `templates/principal/vacinas.html`
- `templates/principal/vacina_list.html`
- `templates/principal/vacina_detail.html`
- `templates/principal/vacina_form.html`
- `templates/principal/vacina_confirm_delete.html`

---

### Suellen Vitória — Tela Inicial e Login

**Responsabilidades:**

- Desenvolver a tela inicial;
- Desenvolver a tela de login;
- Organizar a navegação inicial do sistema;
- Trabalhar na apresentação visual da página inicial;
- Desenvolver ou modificar os arquivos necessários para essas funcionalidades.

**Principais arquivos:**

- `principal/views.py`
- `principal/urls.py`
- `templates/principal/home.html`
- `templates/principal/base.html`
- Arquivos CSS em `principal/static/`
