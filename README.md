
# Desafio Fabrica de Software 2025.2

O desafio consistia em criar um ambiente web com um CRUD funcionando com 02 ou mais entidades com o framework django, utilizando o CBV(ClassBasedViews).

Diferenciais seriam utilizar um banco externo (O banco utilizado foi o MySQL), e a capacidade de poder criar tokens de autenticação. 

O sistema desenvolvido, foi basicamente um gerenciador de Livros, Autores e Usuários, desenvolvido em django, utilizando uma api de busca do googlebooks, e com CRUD's para gerenciar todas as entidades. Além disso foi feita uma instalação de um banco de daods externo (MySQL), e também foi adicionada a capacidade de gerar tokens de autenticação.

# Tecnologias Utilizadas

- Python 3.10.0
- Django 5.2.6
- requests
- MySQL 8.0
- Rest_Framework
- Rest_Framework.authtoken


## 1. Criação do Ambiente Virtual

Clonar o repositório do github e entrar na pasta do projeto

```bash
  git clone <https://github.com/EdsonJr99/wsBackend-Fabrica25.2>
  cd PythonProjeto
```
## 2. Criar e ativar o Ambiente Virtual

Criação e Ativação da .venv

```bash
  python -m venv .venv .
  .\.venv\Scripts\activate
```

## 3. Atualizar pip

```bash
  python -m pip install --upgrade.pip
```

## 4. Instalar dependências

```bash
  pip install -r requirements.txt
```

## 5. Criar e realizar migrações no banco de dados

```bash
  python manage.py makemigrations
  python manage.py migrate
```

## 6. Criar super usuário

Necessário para o acesso da pagina django/admin

```bash
  python manage.py createsuperuser
```

## 7. Executar o servidor local

```bash
  python manage.py runserver
```

## Links

A aplicação ficará disponível nas seguintes URL's:

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/