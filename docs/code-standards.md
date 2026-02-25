# Padroes de Codigo

## Regras Gerais

- Codigo Python segue **PEP 8**
- Usar **aspas simples** (`'texto'`) em todo o codigo Python
- Todo o codigo (variaveis, funcoes, classes, comentarios) deve ser escrito em **ingles**
- A interface do usuario (templates, labels, mensagens) deve ser em **portugues brasileiro**

## Django

### Views

- Usar **Class-Based Views (CBV)** sempre que possivel
- Views autenticadas devem usar `LoginRequiredMixin`
- Querysets de dados do usuario devem sempre filtrar por `user=request.user`

### Models

- Toda model deve ter os campos `created_at` (auto_now_add) e `updated_at` (auto_now)
- Implementar `__str__` em todas as models

### Signals

- Signals devem ficar em arquivos `signals.py` dentro de cada app

### Forms

- Usar `ModelForm` para formularios vinculados a models
- Estilizar widgets com classes TailwindCSS no `__init__` ou `Meta.widgets`

### URLs

- Usar namespaces para cada app (ex: `assets:list`, `transactions:create`)
- URLs em portugues para o usuario final (ex: `/ativos/`, `/transacoes/`)

## Estrutura de Arquivos por App

```
app_name/
├── models.py       # Models do banco de dados
├── views.py        # Views (CBV)
├── forms.py        # Formularios
├── urls.py         # Rotas da app
├── admin.py        # Configuracao do admin
├── signals.py      # Signals/eventos
├── services.py     # Logica de negocio (quando necessario)
├── tests.py        # Testes
└── migrations/     # Migracoes do banco
```

## Templates

- Templates base ficam em `templates/` na raiz do projeto
- Templates de app ficam em `templates/<app_name>/`
- Componentes reutilizaveis ficam em `templates/components/`
- Heranca de templates via `{% extends "base.html" %}` e `{% block content %}`

## Principio Geral

O projeto deve ser **simples e enxuto, sem over engineering**. Nao adicionar features, abstracoes ou complexidade alem do necessario.
