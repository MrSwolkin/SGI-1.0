# Stack Tecnologica

## Camadas

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Framework Web | Django 6.x |
| Frontend | Django Template Language + TailwindCSS (CDN) |
| Banco de Dados | SQLite (nativo Django) |
| Autenticacao | Django Auth (customizado para email) |
| Graficos | Chart.js (via CDN) |
| Ambiente | virtualenv + pip |

## Dependencias (requirements.txt)

| Pacote | Versao | Finalidade |
|---|---|---|
| Django | 6.0.2 | Framework web |
| asgiref | 3.11.1 | Compatibilidade ASGI |
| sqlparse | 0.5.5 | Parsing SQL |
| pandas | 3.0.1 | Manipulacao de dados |
| numpy | 2.4.2 | Computacao numerica |
| openpyxl | 3.1.5 | Leitura de arquivos Excel (.xlsx) |
| python-dateutil | 2.9.0 | Utilitarios de data |
| et_xmlfile | 2.0.0 | Manipulacao XML (dependencia do openpyxl) |
| six | 1.17.0 | Compatibilidade Python (dependencia) |

## Frontend (via CDN)

As dependencias de frontend sao carregadas via CDN diretamente nos templates, sem processo de build:

- **TailwindCSS**: Framework CSS utilitario
- **Google Fonts (Inter)**: Tipografia do design system
- **Chart.js**: Biblioteca de graficos (doughnut chart para composicao da carteira)
