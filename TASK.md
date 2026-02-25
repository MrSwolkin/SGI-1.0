### Sprint 0 — Configuração do Projeto ✅

#### Tarefa 0.1 — Ambiente e dependências
- [X] 0.1.1 Criar e ativar o ambiente virtual Python (`python -m venv .venv`)
- [X] 0.1.2 Instalar Django (`pip install django`)
- [X] 0.1.3 Criar arquivo `requirements.txt` com as dependências iniciais
- [X] 0.1.4 Verificar a estrutura de diretórios do projeto conforme a arquitetura definida

#### Tarefa 0.2 — Configurações do Django (`core/settings.py`) ✅
- [X] 0.2.1 Configurar `INSTALLED_APPS` com as apps: `assets`, `portfolios`, `transactions`
- [X] 0.2.2 Configurar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'`
- [X] 0.2.3 Configurar `DATABASES` para SQLite
- [X] 0.2.4 Configurar `STATIC_URL` e `STATICFILES_DIRS`
- [X] 0.2.5 Configurar `TEMPLATES` com `DIRS` apontando para a pasta `templates/`
- [X] 0.2.6 Configurar `LOGIN_URL`, `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`
- [X] 0.2.7 Definir `AUTH_USER_MODEL` para o modelo customizado de usuário

#### Tarefa 0.3 — Usuário customizado (login por email) ✅
- [X] 0.3.1 Criar app `accounts` com `python manage.py startapp accounts`
- [X] 0.3.2 Criar model `CustomUser` extendendo `AbstractUser` dentro de `accounts/models.py`
- [X] 0.3.3 Sobrescrever campo `USERNAME_FIELD = 'email'` e `REQUIRED_FIELDS = ['first_name', 'last_name']`
- [X] 0.3.4 Definir campo `email` como `unique=True`
- [X] 0.3.5 Criar `CustomUserManager` estendendo `BaseUserManager` com métodos `create_user` e `create_superuser`
- [X] 0.3.6 Registrar `AUTH_USER_MODEL = 'accounts.CustomUser'` no `settings.py`
- [X] 0.3.7 Criar e executar as migrações iniciais (`makemigrations` + `migrate`)

#### Tarefa 0.4 — URLs principais ✅
- [X] 0.4.1 Configurar `core/urls.py` com include para as apps: `accounts`, `assets`, `transactions`, `portfolios`
- [X] 0.4.2 Adicionar rota para a landing page pública na raiz `/`

---

### Sprint 1 — Design System e Templates Base ✅

#### Tarefa 1.1 — Estrutura de templates ✅
- [X] 1.1.1 Criar pasta `templates/` na raiz do projeto
- [X] 1.1.2 Criar subpastas: `templates/accounts/`, `templates/assets/`, `templates/transactions/`, `templates/portfolios/`, `templates/public/`
- [X] 1.1.3 Criar arquivo `templates/base.html` com o layout base do sistema autenticado
- [X] 1.1.4 Criar arquivo `templates/public/base_public.html` com layout base para páginas públicas

#### Tarefa 1.2 — Implementar `base.html` (área autenticada) ✅
- [X] 1.2.1 Adicionar `<head>` com meta tags, title block, importação do TailwindCSS via CDN e fonte Inter
- [X] 1.2.2 Implementar sidebar de navegação com logo Finanpy (gradiente violeta/índigo)
- [X] 1.2.3 Adicionar links de navegação na sidebar: Dashboard, Transações, Ativos
- [X] 1.2.4 Implementar estado ativo no link de navegação usando `request.resolver_match.url_name`
- [X] 1.2.5 Adicionar informações do usuário e botão de logout no rodapé da sidebar
- [X] 1.2.6 Implementar área `main` com `{% block content %}{% endblock %}`
- [X] 1.2.7 Adicionar área de mensagens (Django messages framework) com estilos de sucesso/erro/aviso
- [X] 1.2.8 Garantir que o layout seja responsivo com menu hamburguer para mobile (TailwindCSS)

#### Tarefa 1.3 — Implementar `base_public.html` ✅
- [X] 1.3.1 Criar header com logo e links de Cadastro e Login
- [X] 1.3.2 Implementar fundo escuro com gradiente sutil
- [X] 1.3.3 Adicionar footer simples com nome do produto

#### Tarefa 1.4 — Componentes reutilizáveis (includes) ✅
- [X] 1.4.1 Criar `templates/components/card_metric.html` para cards de métricas do dashboard
- [X] 1.4.2 Criar `templates/components/table.html` como estrutura base de tabelas
- [X] 1.4.3 Criar `templates/components/form_field.html` para renderização padronizada de campos de formulário
- [X] 1.4.4 Criar `templates/components/badge.html` para badges de tipo (Compra/Venda, tipo de ativo)
- [X] 1.4.5 Criar `templates/components/empty_state.html` para estado de lista vazia

---

### Sprint 2 — Site Público e Autenticação ✅

#### Tarefa 2.1 — Landing Page ✅
- [X] 2.1.1 Criar view `LandingPageView` (TemplateView) em `accounts/views.py` ou em uma view standalone
- [X] 2.1.2 Criar template `templates/public/landing.html` extendendo `base_public.html`
- [X] 2.1.3 Implementar seção hero com título, subtítulo e botões de Cadastro e Login
- [X] 2.1.4 Implementar seção de features resumidas do produto
- [X] 2.1.5 Configurar URL `/` apontando para `LandingPageView`
- [X] 2.1.6 Redirecionar usuário já autenticado para o dashboard ao acessar a landing page

#### Tarefa 2.2 — Formulário de Cadastro ✅
- [X] 2.2.1 Criar `CustomUserCreationForm` em `accounts/forms.py` com campos: `first_name`, `last_name`, `email`, `password1`, `password2`
- [X] 2.2.2 Adicionar validação de email único no `clean_email()`
- [X] 2.2.3 Criar `RegisterView` (FormView ou CreateView) em `accounts/views.py`
- [X] 2.2.4 Criar template `templates/accounts/register.html` com o formulário de cadastro estilizado
- [X] 2.2.5 Após cadastro, redirecionar para a tela de login com mensagem de sucesso
- [X] 2.2.6 Configurar URL `/cadastro/` para `RegisterView`

#### Tarefa 2.3 — Formulário de Login ✅
- [X] 2.3.1 Criar `EmailAuthenticationForm` em `accounts/forms.py` extendendo `AuthenticationForm` para usar email
- [X] 2.3.2 Criar `CustomLoginView` extendendo `LoginView` do Django com `form_class = EmailAuthenticationForm`
- [X] 2.3.3 Criar template `templates/accounts/login.html` com formulário de login estilizado
- [X] 2.3.4 Configurar URL `/login/` para `CustomLoginView`

#### Tarefa 2.4 — Logout ✅
- [X] 2.4.1 Usar a `LogoutView` nativa do Django
- [X] 2.4.2 Configurar URL `/logout/` e `LOGOUT_REDIRECT_URL = '/'` no settings
- [X] 2.4.3 Adicionar link de logout na sidebar do `base.html`

---

### Sprint 3 — App de Ativos (Assets)

#### Tarefa 3.1 — Model `Asset`
- [ ] 3.1.1 Criar model `Asset` em `assets/models.py` com campos: `ticker` (CharField, unique), `name` (CharField), `asset_type` (CharField com choices: STOCK, FII, ETF, INTERNATIONAL), `currency` (CharField com choices: BRL, USD)
- [ ] 3.1.2 Adicionar campos `created_at` (auto_now_add) e `updated_at` (auto_now)
- [ ] 3.1.3 Implementar método `__str__` retornando `f'{self.ticker} - {self.name}'`
- [ ] 3.1.4 Criar e executar a migração do model Asset

#### Tarefa 3.2 — Admin do Asset
- [ ] 3.2.1 Registrar `Asset` no `assets/admin.py` com `list_display`, `search_fields` e `list_filter`

#### Tarefa 3.3 — Form de Asset
- [ ] 3.3.1 Criar `AssetForm` em `assets/forms.py` usando `ModelForm`
- [ ] 3.3.2 Estilizar os widgets do form com as classes Tailwind do design system

#### Tarefa 3.4 — Views de Asset
- [ ] 3.4.1 Criar `AssetListView` (ListView) em `assets/views.py` com `LoginRequiredMixin`
- [ ] 3.4.2 Criar `AssetCreateView` (CreateView) com `LoginRequiredMixin`
- [ ] 3.4.3 Configurar `success_url` com `reverse_lazy('assets:list')`
- [ ] 3.4.4 Adicionar mensagem de sucesso ao criar ativo

#### Tarefa 3.5 — Templates de Asset
- [ ] 3.5.1 Criar `templates/assets/asset_list.html` com tabela de ativos e botão de novo ativo
- [ ] 3.5.2 Criar `templates/assets/asset_form.html` com formulário de criação de ativo
- [ ] 3.5.3 Tratar estado de lista vazia usando o componente `empty_state.html`

#### Tarefa 3.6 — URLs de Asset
- [ ] 3.6.1 Criar `assets/urls.py` com rotas: `list` (`/ativos/`) e `create` (`/ativos/novo/`)
- [ ] 3.6.2 Incluir `assets/urls.py` no `core/urls.py` com namespace `assets`

---

### Sprint 4 — App de Transações (Transactions)

#### Tarefa 4.1 — Model `Transaction`
- [ ] 4.1.1 Criar model `Transaction` em `transactions/models.py` com campos: `user` (FK para `settings.AUTH_USER_MODEL`), `asset` (FK para `Asset`), `transaction_type` (CharField choices: BUY, SELL), `quantity` (DecimalField), `unit_price` (DecimalField), `fee` (DecimalField, default=0), `operation_date` (DateField)
- [ ] 4.1.2 Adicionar campos `created_at` e `updated_at`
- [ ] 4.1.3 Implementar `__str__` retornando tipo, ticker e data
- [ ] 4.1.4 Criar propriedade `total_value` calculando `quantity * unit_price + fee`
- [ ] 4.1.5 Criar e executar migração do model Transaction

#### Tarefa 4.2 — Admin de Transaction
- [ ] 4.2.1 Registrar `Transaction` no `transactions/admin.py` com `list_display`, `list_filter` e `search_fields`

#### Tarefa 4.3 — Form de Transaction
- [ ] 4.3.1 Criar `TransactionForm` em `transactions/forms.py` usando `ModelForm`
- [ ] 4.3.2 Excluir o campo `user` do formulário (será preenchido na view)
- [ ] 4.3.3 Adicionar widget `DateInput` com `type='date'` para `operation_date`
- [ ] 4.3.4 Estilizar todos os widgets com as classes Tailwind do design system

#### Tarefa 4.4 — Views de Transaction
- [ ] 4.4.1 Criar `TransactionListView` (ListView) com `LoginRequiredMixin`, filtrando apenas transações do usuário logado
- [ ] 4.4.2 Criar `TransactionCreateView` (CreateView) com `LoginRequiredMixin`
- [ ] 4.4.3 Sobrescrever `form_valid` para associar `form.instance.user = self.request.user`
- [ ] 4.4.4 Criar `TransactionUpdateView` (UpdateView) com `LoginRequiredMixin`
- [ ] 4.4.5 Sobrescrever `get_queryset` para garantir que o usuário só edite suas próprias transações
- [ ] 4.4.6 Criar `TransactionDeleteView` (DeleteView) com `LoginRequiredMixin` e mesmo filtro de queryset
- [ ] 4.4.7 Adicionar mensagens de sucesso em create, update e delete

#### Tarefa 4.5 — Templates de Transaction
- [ ] 4.5.1 Criar `templates/transactions/transaction_list.html` com tabela de transações e badges coloridos por tipo
- [ ] 4.5.2 Criar `templates/transactions/transaction_form.html` para criação e edição
- [ ] 4.5.3 Criar `templates/transactions/transaction_confirm_delete.html` com modal/página de confirmação
- [ ] 4.5.4 Implementar filtro por ativo e tipo usando GET params no `TransactionListView`
- [ ] 4.5.5 Tratar estado vazio com componente `empty_state.html`

#### Tarefa 4.6 — URLs de Transaction
- [ ] 4.6.1 Criar `transactions/urls.py` com rotas: `list`, `create`, `update/<pk>/`, `delete/<pk>/`
- [ ] 4.6.2 Incluir no `core/urls.py` com namespace `transactions`

---

### Sprint 5 — Dashboard e Portfólio

#### Tarefa 5.1 — Lógica de portfólio
- [ ] 5.1.1 Criar arquivo `portfolios/services.py` com função `get_portfolio_summary(user)` que retorna dados consolidados da carteira
- [ ] 5.1.2 A função deve calcular: total investido (soma de compras - soma de vendas), lista de ativos com saldo positivo, quantidade e preço médio ponderado por ativo
- [ ] 5.1.3 Criar função `get_composition_by_type(user)` retornando o percentual investido por tipo de ativo

#### Tarefa 5.2 — View do Dashboard
- [ ] 5.2.1 Criar `DashboardView` (TemplateView ou View) em `portfolios/views.py` com `LoginRequiredMixin`
- [ ] 5.2.2 No `get_context_data`, chamar `get_portfolio_summary` e `get_composition_by_type` e passar os resultados para o template
- [ ] 5.2.3 Passar os dados do gráfico como JSON serializado para o template

#### Tarefa 5.3 — Template do Dashboard
- [ ] 5.3.1 Criar `templates/portfolios/dashboard.html` extendendo `base.html`
- [ ] 5.3.2 Implementar grid de 4 cards de métricas (total investido, nº de ativos, maior posição, última transação)
- [ ] 5.3.3 Implementar gráfico de composição por tipo usando Chart.js (doughnut chart)
- [ ] 5.3.4 Implementar tabela resumida das posições em carteira (ativo, quantidade, preço médio, valor atual estimado)
- [ ] 5.3.5 Exibir estado vazio quando não há transações cadastradas

#### Tarefa 5.4 — URLs do Dashboard
- [ ] 5.4.1 Criar `portfolios/urls.py` com rota `/dashboard/` para `DashboardView`
- [ ] 5.4.2 Incluir no `core/urls.py` com namespace `portfolios`
- [ ] 5.4.3 Configurar `LOGIN_REDIRECT_URL = '/dashboard/'` no `settings.py`

---

### Sprint 6 — Ajustes Finais e Polimento

#### Tarefa 6.1 — Página 404 customizada
- [ ] 6.1.1 Criar template `templates/404.html` com layout do design system
- [ ] 6.1.2 Configurar handler404 no `core/urls.py`

#### Tarefa 6.2 — Mensagens globais
- [ ] 6.2.1 Revisar todos os formulários e garantir que mensagens de sucesso e erro estão sendo exibidas corretamente via Django messages framework
- [ ] 6.2.2 Garantir que as mensagens somem após a exibição (auto-dismiss com JS simples ou via Tailwind)

#### Tarefa 6.3 — Segurança básica
- [ ] 6.3.1 Verificar que todas as views autenticadas possuem `LoginRequiredMixin`
- [ ] 6.3.2 Verificar que querysets de transações sempre filtram por `user=request.user`
- [ ] 6.3.3 Garantir que o token CSRF está presente em todos os formulários `{% csrf_token %}`

#### Tarefa 6.4 — Revisão de responsividade
- [ ] 6.4.1 Testar todas as telas em viewport mobile (375px)
- [ ] 6.4.2 Testar em viewport tablet (768px)
- [ ] 6.4.3 Testar em viewport desktop (1280px+)
- [ ] 6.4.4 Corrigir problemas de layout identificados

#### Tarefa 6.5 — Dados iniciais
- [ ] 6.5.1 Criar arquivo `assets/fixtures/initial_assets.json` com alguns ativos populares pré-cadastrados (ex: PETR4, MXRF11, BOVA11, IVVB11)
- [ ] 6.5.2 Documentar no README como carregar os fixtures: `python manage.py loaddata initial_assets`

#### Tarefa 6.6 — README do projeto
- [ ] 6.6.1 Criar `README.md` com: descrição do projeto, pré-requisitos, instruções de instalação e execução, estrutura de diretórios e como carregar fixtures

---

### Sprint 7 (Final) — Testes e Docker *(planejado)*

#### Tarefa 7.1 — Testes unitários
- [ ] 7.1.1 Configurar ambiente de testes
- [ ] 7.1.2 Escrever testes para a lógica de cálculo de portfólio (`portfolios/services.py`)
- [ ] 7.1.3 Escrever testes para models (validações e propriedades calculadas)
- [ ] 7.1.4 Escrever testes de integração para as views principais

#### Tarefa 7.2 — Docker
- [ ] 7.2.1 Criar `Dockerfile` para a aplicação Django
- [ ] 7.2.2 Criar `docker-compose.yml` com serviço web
- [ ] 7.2.3 Testar build e execução via Docker
- [ ] 7.2.4 Atualizar README com instruções de execução via Docker

---