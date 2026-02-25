# Setup do Ambiente

## Pre-requisitos

- Python 3.12+
- pip

## Instalacao

1. Clone o repositorio e entre na pasta do projeto:

```bash
cd SGI
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Execute as migracoes do banco de dados:

```bash
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

O projeto estara disponivel em `http://127.0.0.1:8000/`.

## Criando um Superusuario

Para acessar o painel admin do Django (`/admin/`):

```bash
python manage.py createsuperuser
```

## Estrutura de Comandos Uteis

| Comando | Descricao |
|---|---|
| `python manage.py runserver` | Inicia o servidor de desenvolvimento |
| `python manage.py migrate` | Aplica migracoes pendentes no banco |
| `python manage.py makemigrations` | Gera novas migracoes a partir dos models |
| `python manage.py createsuperuser` | Cria usuario administrador |
| `python manage.py test` | Executa os testes |
| `python manage.py shell` | Abre o shell interativo do Django |
