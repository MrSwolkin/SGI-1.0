# Design System

O design e implementado com **TailwindCSS via CDN** dentro do **Django Template Language**. Tema escuro com gradientes violet/indigo.

## Paleta de Cores

| Token | Classe Tailwind | Hex | Uso |
|---|---|---|---|
| Background principal | `bg-gray-950` | #030712 | Fundo das paginas |
| Background card | `bg-gray-900` | #111827 | Cards e paineis |
| Background input | `bg-gray-800` | #1f2937 | Campos de formulario |
| Borda sutil | `border-gray-700` | #374151 | Bordas de cards/inputs |
| Primaria (gradiente) | `from-violet-600 to-indigo-600` | — | Botoes e destaques principais |
| Destaque | `text-violet-400` | #a78bfa | Links e icones ativos |
| Texto principal | `text-gray-100` | #f3f4f6 | Textos primarios |
| Texto secundario | `text-gray-400` | #9ca3af | Labels e textos auxiliares |
| Sucesso | `text-emerald-400` | #34d399 | Valores positivos, compras |
| Perigo | `text-red-400` | #f87171 | Valores negativos, vendas |
| Aviso | `text-yellow-400` | #facc15 | Alertas |

## Tipografia

- **Fonte**: Inter (Google Fonts)
- **Pesos**: 300, 400, 500, 600, 700

| Elemento | Classes |
|---|---|
| Titulo de pagina | `text-3xl font-bold text-gray-100` |
| Subtitulo | `text-xl font-semibold text-gray-200` |
| Label de secao | `text-sm font-medium text-gray-400 uppercase tracking-wider` |
| Texto corrido | `text-sm text-gray-300 leading-relaxed` |

## Botoes

| Tipo | Uso | Estilo principal |
|---|---|---|
| Primario | Acoes principais (salvar, confirmar) | Gradiente violet-600 → indigo-600 |
| Secundario | Acoes alternativas (cancelar) | Outline com border-gray-600 |
| Perigo | Acoes destrutivas (excluir) | bg-red-600/20 com border-red-600/50 |
| Acao/Pequeno | Links de acao em tabelas | text-violet-400, sem fundo |

## Inputs e Formularios

- Background: `bg-gray-800`
- Borda: `border-gray-700`
- Focus: `ring-2 ring-violet-500`
- Erro: `text-xs text-red-400`
- Card de formulario: `bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-xl`

## Cards

- **Card de metrica**: `bg-gray-900 border border-gray-800 rounded-xl p-5 shadow-lg`
- **Card de lista**: Mesmo estilo com header separado por `border-b border-gray-800`

## Tabelas

- Container: `bg-gray-900 border border-gray-800 rounded-xl overflow-hidden`
- Header: `text-xs font-medium text-gray-400 uppercase tracking-wider`
- Linhas: `divide-y divide-gray-800` com `hover:bg-gray-800/50`

## Layout

- **Sidebar**: `w-64 bg-gray-900 border-r border-gray-800`, com logo em gradiente violet/indigo
- **Conteudo principal**: `max-w-7xl mx-auto px-6 py-8`
- **Grid de metricas**: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4`
- **Grid de conteudo**: `grid grid-cols-1 lg:grid-cols-3 gap-6`
- **Responsivo**: Mobile-first com breakpoints sm/lg

## Navegacao

- Link ativo: `text-violet-400 bg-violet-500/10 border border-violet-500/20`
- Link inativo: `text-gray-300 hover:text-gray-100 hover:bg-gray-800`
