# Agentes de Desenvolvimento — SGI

Time de agentes de IA especializados na stack do projeto.

## Agentes

| Agente | Arquivo | Quando usar |
|---|---|---|
| Backend Django | [backend.md](backend.md) | Models, views, forms, URLs, services, signals, admin, migrations |
| Frontend DTL + Tailwind | [frontend.md](frontend.md) | Templates HTML, componentes, estilizacao TailwindCSS, Chart.js, responsividade |
| QA Tester | [qa-tester.md](qa-tester.md) | Testes end-to-end via navegador, validacao visual do design, verificacao de fluxos |

## Como usar

Cada arquivo `.md` contem o system prompt completo do agente. Copie o conteudo do arquivo e use como instrucao do agente na ferramenta de IA de sua preferencia.

Os agentes de implementacao (Backend e Frontend) utilizam o **MCP server Context7** para consultar documentacao atualizada das tecnologias antes de escrever codigo.

O agente de QA utiliza o **MCP server Playwright** para acessar o sistema via navegador e validar funcionalidades e design.

## Referencia rapida

- PRD completo: `PRD.md`
- Documentacao do projeto: `docs/README.md`
- Design system: `docs/design-system.md`
- Padroes de codigo: `docs/code-standards.md`
- Modelos de dados: `docs/data-models.md`
