# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**SGI** — Django full-stack monolith for personal variable income investment management (stocks, FIIs, ETFs, international stocks). Server-side rendered with Django Template Language + TailwindCSS (CDN). SQLite database. See `PRD.md` for full requirements and sprint planning.

## Commands

```bash
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run
python manage.py runserver

# Database
python manage.py makemigrations
python manage.py migrate

# Tests
python manage.py test
python manage.py test <app_name>
```

## Architecture

Django project (`core/`) with 3 apps:
- **assets/** — Financial assets (stocks, FIIs, ETFs, international stocks)
- **transactions/** — Buy/sell transaction records
- **portfolios/** — Dashboard with portfolio summary and charts

Data flow: Templates → Views (CBV) → Forms → Models (ORM) → SQLite

Portfolio values are calculated dynamically from transactions (no stored aggregates). Business logic for calculations goes in `services.py` files (e.g., `portfolios/services.py`).

### Data Model Relationships

```
User ||--o{ Transaction (user FK)
Asset ||--o{ Transaction (asset FK)
User ||--o| Portfolio (1-to-1)
```

Four models: CustomUser (email-based auth via AbstractUser), Asset (ticker, type, currency), Transaction (user, asset, type BUY/SELL, quantity, unit_price, fee, operation_date), Portfolio (user 1-to-1).

All models must have `created_at` (auto_now_add) and `updated_at` (auto_now).

## Code Conventions

- **Python**: PEP 8, single quotes (`'text'`), code in English
- **UI text**: Portuguese Brazilian (templates, labels, messages, URLs)
- **Views**: Always Class-Based Views with `LoginRequiredMixin` for authenticated routes
- **Querysets**: Always filter by `user=request.user` for user-scoped data
- **Forms**: `ModelForm` with TailwindCSS widget styling
- **URLs**: Namespaced per app (`assets:list`, `transactions:create`), paths in Portuguese (`/ativos/`, `/transacoes/`)
- **Signals**: In `signals.py` within each app
- **Principle**: Simple and lean, no over-engineering

### App File Structure

```
app_name/
├── models.py       # Database models
├── views.py        # Class-Based Views
├── forms.py        # ModelForms
├── urls.py         # App routes
├── admin.py        # Admin config
├── signals.py      # Event handlers
├── services.py     # Business logic
├── tests.py        # Tests
└── migrations/
```

### Templates

- Base templates: `templates/` (project root)
- App templates: `templates/<app_name>/`
- Reusable components: `templates/components/`
- Public pages: `templates/public/`
- Inheritance: `{% extends "base.html" %}` + `{% block content %}`

## Design System

Dark theme with violet/indigo gradients. TailwindCSS via CDN, Inter font via Google Fonts, Chart.js via CDN for charts.

Key tokens:
- Page background: `bg-gray-950`
- Cards: `bg-gray-900 border border-gray-800 rounded-xl`
- Inputs: `bg-gray-800 border-gray-700`, focus `ring-violet-500`
- Primary action: gradient `from-violet-600 to-indigo-600`
- Active nav: `text-violet-400 bg-violet-500/10`
- Success/buy: `text-emerald-400` | Danger/sell: `text-red-400`

Full design system reference with HTML examples: `docs/design-system.md`

## Documentation

All project docs are in `docs/` — see `docs/README.md` for the index.
