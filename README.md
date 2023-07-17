# Pagina de cadastro e login

Aplicação Django com login e cadastro completo: front-end e back-end implementados em Django.

## Sumário

- [Instalação](#instalação)
- [Uso Local](#uso-local)
- [Documentação API](#Rotas)

## Instalação

Para inciar este projeto, é necessário instalar as dependências. Para fazer a instalação basta dar o seguinte comando:

```
pip install -r requirements.txt
```

## Uso Local

1. Execute as migrations do banco de dados:

```bash
python manage.py migrate
```

2. Inicie o servidor:

```bash
python manage.py runserver
```

3. As rotas podem ser acessadas pelo endereço:

```bash
http://127.0.0.1:8000/api/login
```

## Rotas

Essa aplicação possui três rotas

# Página de login
```bash
http://127.0.0.1:8000/api/login
```

# Pagina de Cadastro
```bash
http://127.0.0.1:8000/api/register
```

# Dashboard em contrução.
Obs: É preciso estar logado para acessar.
```bash
http://127.0.0.1:8000/api/dashboard
```
