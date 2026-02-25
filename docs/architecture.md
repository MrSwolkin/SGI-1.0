# Arquitetura do Projeto

## Tipo de Aplicacao

Monolito full-stack Django com renderizacao server-side (Django Template Language + TailwindCSS).

## Estrutura de Pastas

```
SGI/
├── core/                   # Projeto Django (configuracoes centrais)
│   ├── settings.py         # Configuracoes do Django
│   ├── urls.py             # Rotas principais
│   ├── wsgi.py             # Entry point WSGI
│   └── asgi.py             # Entry point ASGI
│
├── assets/                 # App: Gestao de ativos financeiros
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
│
├── transactions/           # App: Registro de transacoes (compra/venda)
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
│
├── portfolios/             # App: Dashboard e analise de carteira
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
│
├── db.sqlite3              # Banco de dados SQLite
├── manage.py               # CLI do Django
├── requirements.txt        # Dependencias Python
├── PRD_finanpy.md          # Documento de requisitos do produto
└── docs/                   # Documentacao do projeto
```

## Apps Django

O projeto esta organizado em 3 apps:

| App | Responsabilidade |
|---|---|
| `assets` | Cadastro e listagem de ativos (acoes, FIIs, ETFs, stocks) |
| `transactions` | Registro, edicao e exclusao de transacoes de compra e venda |
| `portfolios` | Dashboard com resumo consolidado da carteira e graficos |

## Fluxo de Dados

```
Usuario → Templates (Django DTL + TailwindCSS)
            ↓
         Views (Class-Based Views)
            ↓
         Forms (validacao)
            ↓
         Models (ORM)
            ↓
         SQLite
```

## Decisoes Arquiteturais

- **Server-side rendering**: Sem SPA. O frontend e renderizado via Django Templates + TailwindCSS (CDN).
- **Class-Based Views (CBV)**: Todas as views devem usar CBVs do Django.
- **SQLite**: Banco de dados nativo do Django, sem necessidade de servidor externo.
- **Autenticacao nativa**: Sistema de autenticacao do Django customizado para login por email.
- **Graficos via CDN**: Chart.js carregado via CDN, sem build frontend.
