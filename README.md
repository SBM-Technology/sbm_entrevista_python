# Interview SBM – Dashboard de Vendas

## Visão Geral
Aplicação web em Flask para explorar dados de vendas com dashboards (Chart.js) e análises no backend (SQLAlchemy + Pandas). Inclui KPIs, séries temporais, vendas por categoria/região, margem de lucro por produto, médias móveis e sazonalidade por dia da semana.

---

## 1) Instruções de setup e execução

- Pré‑requisitos
  - Python 3.11+
  - Pip

- Clonar e instalar dependências
  - Criar ambiente virtual
    - Windows (PowerShell):
      - `python -m venv venv`
      - `venv\Scripts\Activate.ps1`
    - macOS/Linux:
      - `python3 -m venv venv`
      - `source venv/bin/activate`
  - Instalar pacotes
    - `pip install -r requirements.txt`

### Testes automatizados

- Executar a suíte de testes:
  - `pytest -q`
- Executar com cobertura de código:
  - `pytest -q --cov=app --cov-report=term-missing`
- Estrutura dos testes:
  - `tests/conftest.py`: fixtures (app em modo teste, banco em memória, seed mínimo)
  - `tests/test_routes_dashboard.py`: testes das rotas do dashboard (KPIs, séries temporais, categoria, região, top produtos, margem, dia da semana)

- Executar a aplicação
  - `python run.py`
  - A aplicação iniciará (por padrão) em `http://127.0.0.1:5100`
  - Banco SQLite em `instance/dashboard.db` será inicializado se necessário

- (Opcional) Dados de exemplo
  - Há scripts em `scripts/` (ex.: `generate_sample_data.py`, `import_initial_data.py`) que podem auxiliar na carga de dados para testes.

---

## 2) Decisões técnicas tomadas

- Backend (Flask + SQLAlchemy)
  - Organização por blueprints e camada de serviço (`app/services/analytics.py`) para manter queries/agrupamentos isolados da view.
  - Uso de agregações SQL para performance e simplicidade (ex.: somatórios, group by por data/categoria/região, join com custos para calcular margem).
  - Mantido join dinamicamente entre `Venda` e `Custo` para margem de lucro (normalização dos dados, sem denormalizar custo na venda) — adequado para o escopo e claro para avaliação.
  - Filtro de datas centralizado em `_aplicar_filtro_data` (robusto a erros de parsing).
  - Ordenação por maior margem feita no SQL com `NULLIF` para evitar divisão por zero.

## 2.1) Documentação da API (endpoints)

Formato padrão
- Método: GET
- Datas: `YYYY-MM-DD` via query string (`data_inicio`, `data_fim`)
- Retorno: JSON, 200 em caso de sucesso

Endpoints
- `/data/kpis`
  - Params: `data_inicio` (opcional), `data_fim` (opcional)
  - Retorno: `{ receita_total: number, num_vendas: number, ticket_medio: number }`

- `/data/vendas-tempo`
  - Params: `data_inicio` (opcional), `data_fim` (opcional)
  - Retorno: `{ labels: string[], valores: number[], quantidades: number[], media_movel_7: (number|null)[], media_movel_30: (number|null)[] }`

- `/data/vendas-categoria`
  - Params: `data_inicio` (opcional), `data_fim` (opcional)
  - Retorno: `{ labels: string[], valores: number[] }`

- `/data/vendas-regiao`
  - Params: `data_inicio` (opcional), `data_fim` (opcional)
  - Retorno: `{ labels: string[], valores: number[], percentuais: number[] }`

- `/data/top-produtos`
  - Params: `data_inicio` (opcional), `data_fim` (opcional), `limite` (opcional, default 10)
  - Retorno: `{ labels: string[], valores: number[], quantidades: number[] }`

- `/data/vendas-margem-lucro`
  - Params: `data_inicio` (opcional), `data_fim` (opcional)
  - Retorno: `{ labels: string[], lucro: number[], receita: number[], margem: number[] }`
  - Observação: ordenado por `margem` decrescente no backend

- `/data/vendas-dia-semana`
  - Params: `data_inicio` (opcional), `data_fim` (opcional)
  - Retorno: `{ labels: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb'], valores: number[], quantidades: number[] }`

- `/data/vendas-vendedor`
  - Params: `data_inicio` (opcional), `data_fim` (opcional), `limite` (opcional, default 10 para gráfico; 50 para tabela)
  - Retorno: `{ labels: string[], valores: number[], quantidades: number[], ticket_medio: number[], percentual_receita: number[], ranking: number[] }`

Notas

- Análises implementadas
  - Série temporal de vendas com médias móveis de 7 e 30 dias (Pandas) para evidenciar tendência.
  - Sazonalidade por dia da semana agregando por `strftime('%w')` (0=Dom…6=Sáb) e retornando valores/quantidades.
  - Margem de lucro por produto (lucro, receita e margem %) com tooltip detalhado no front.

- Frontend (Chart.js)
  - Gráfico de linhas para evolução (com MM7 / MM30).
  - Barras para categorias e regiões (pizza para distribuição por região, conforme design original).
  - Barras horizontais para margem por produto (eixo em % com limite 0–100).
  - Barras verticais para dia da semana com 2 eixos (R$ e Unidades) para comparativo claro.
  - Barras horizontais para vendas por vendedor com tooltip detalhado (Receita, Unidades, Ticket médio, % Receita).
  - Tooltips e ticks formatados em pt-BR (moeda e números).
  - Destruição do gráfico anterior antes de recriar para evitar duplicação/memory leaks.

- Banco
  - SQLite para simplicidade local. Índices já presentes nos modelos (data/produto/categoria/região). Para grandes volumes, considerar índices compostos (ex.: `data, produto`).

---

## 3) Dificuldades encontradas

- Alinhamento de endpoints e rotas
  - Harmonização de nomes (ex.: `/data/vendas-margem-lucro` vs `/data/calcular-margem-lucro`) e montagem correta de querystring no JS.

- Compatibilidade SQL para dia da semana
  - Uso de `strftime('%w', data)` funciona no SQLite. Em Postgres/MySQL exigiria ajuste (`extract(dow ...)`/`dayofweek(...)`).

- Médias móveis e valores faltantes
  - Pandas retorna `NaN` no início da janela; convertido para `None` para o Chart.js ignorar pontos faltantes.

- UX do Chart.js
  - Ajuste de eixos, tooltips e múltiplas escalas (R$ vs Unidades) para legibilidade sem poluir o gráfico.

---

## 4) Melhorias futuras

- Metas e desempenho
  - Reintroduzir endpoints de metas por categoria/região com % atingido e UI dedicada (cards, barras empilhadas, heatmap mês × categoria).

- Modelagem de margem
  - Persistir snapshot de `custo_unitario_venda`/`margem_venda` na venda para histórico fiel e queries sem join quando o volume crescer.

- Performance
  - Índices compostos adicionais (`data, produto`, `data, categoria`) e cache leve (ex.: resultados mais consultados).
  - Materialized views para agregados usados com frequência.

- Qualidade e manutenção
  - Testes unitários/integração (pytest) para serviços de analytics e validação de endpoints.
  - Lint/format (ruff/black) e CI simples.
  - Tratamento de erros com mensagens claras no front (fallbacks quando não há dados).

- Experiência do usuário
  - Ordenação dinâmica (por valor/margem) e filtros adicionais (vendedor, produto, faixa de preço).
  - Seletores para alternar entre Valor/Quantidade e linhas/colunas conforme contexto.

---

## Estrutura (resumo)

- `app/`
  - `blueprints/` — rotas do dashboard e API de dados
  - `models/` — `Venda`, `Custo`, `Meta`, etc.
  - `services/analytics/` — serviços analíticos e facade
    - `analytics.py` — facade `Analytics` que orquestra serviços (padrão DI: `x or Class()`)
    - `vendedor.py` — agregações por vendedor (receita, unidades, ticket médio, % receita, ranking)
    - `categoria.py`, `regiao.py`, `margem.py`, `sazonalidade.py`, `series.py` — demais análises
  - `static/js/dashboard.js` — carregamento e renderização dos gráficos (Chart.js)
  - `templates/dashboard/index.html` — layout do dashboard
- `instance/dashboard.db` — banco SQLite
- `scripts/` — utilitários para gerar/importar dados
- `run.py` — inicialização do app

---

## 5) Entregas do desafio (A/B/C/D) — detalhamento

### A1) Margem de lucro (vendas − custos) no dashboard
- Onde
  - Backend: rota `/data/vendas-margem-lucro` (joins entre vendas e custos; ordenação por margem desc no SQL).
  - Front: `static/js/dashboard.js` → `carregarGraficoMargemLucro`.
  - UI: `templates/dashboard/index.html` → card “Margem de lucro entre produtos”.
- O que faz
  - Retorna `labels`, `lucro`, `receita`, `margem` e plota barras horizontais (%). Tooltip detalha lucro/receita/margem.
- Validações
  - Teste `test_vendas_margem_lucro_ordenado_por_margem`: chaves presentes e `margem` desc.
- Observações
  - Agregação adequada ao volume atual; pode evoluir para materialized views se necessário.

### A4) Médias móveis (7 e 30 dias)
- Onde
  - Backend: `/data/vendas-tempo` inclui `media_movel_7` e `media_movel_30`.
  - Front: `carregarGraficoVendasTempo` (Chart.js linha + duas séries de MM).
- O que faz
  - Suaviza série diária; `None` nos inícios de janela para Chart.js ignorar pontos.
- Validações
  - `test_vendas_tempo_ok`: chaves e tamanhos coerentes.

### A5) Ranking de vendedores (métricas de performance)
- Onde
  - Backend: `/data/vendas-vendedor` → `labels`, `valores`, `quantidades`, `ticket_medio`, `percentual_receita`, `ranking`.
  - Front: gráfico e tabela (seções abaixo B1 e B5).
- O que faz
  - Ordena por receita desc e calcula métricas auxiliares; percentuais somam ~100%.
- Validações
  - `test_vendas_desempenho_por_vendedor`: chaves, ordenação desc, soma de percentuais ~100.

### B1) Gráfico de desempenho por vendedor
- Onde
  - Front: `carregarGraficoVendasVendedor` (barras horizontais, eixo X moeda, tooltip rico).
  - UI: `index.html` → seção “Vendas por Vendedor”.
- O que faz
  - Compara vendedores por receita; tooltip mostra também quantidades, ticket e participação.
- Observações
  - Mantido 1 dataset para evitar poluição; demais métricas no tooltip e na tabela.

### B5) Tabela interativa com ordenação e busca
- Onde
  - UI: `index.html` → tabela `#tableVendedores` com `table-responsive` e cabeçalhos com `data-sort`.
  - Front: `dashboard.js`
    - Busca: `wireFiltroVendedores` filtra `_vendorsCache` por nome.
    - Ordenação: implementação DOM-only no final do arquivo (listener em `<thead>` reordena `<tr>` do `<tbody>`; alterna asc/desc via `data-dir`).
- O que faz
  - Busca incremental e ordenação por qualquer coluna sem estado adicional.
- Observações
  - Simples e eficiente para volume moderado; para grandes listas, considerar ordenação server-side.

### B8) Responsividade mobile
- Onde
  - Base: `templates/layouts/base.html` com meta viewport e navbar colapsável (Bootstrap).
  - Grid: `index.html` usa `col-12/col-md-*` para cards/gráficos.
  - Tabela: `table-responsive` aplicado.
  - CSS: `static/css/style.css`
    - Media query ≤768px: `canvas { max-height: 300px }`.
    - Media query ≤576px: `canvas { max-height: 260px }`, `#vendorSearch` full-width, cabeçalhos/células da tabela com quebra de linha, tipografia e padding reduzidos para evitar sobreposição.
- O que faz
  - Garante boa leitura em telas pequenas sem overflow de gráficos e sem títulos “um em cima do outro”.

### C1) Validação do upload de CSV (todos os campos)
- Onde
  - UI: modal em `base.html`; front: `dashboard.js` (`#uploadButton` envia `multipart/form-data` para `/api/upload`).
  - Backend: endpoint valida schema esperado e retorna `error`/`registros`.
- O que faz
  - Restringe tipo de arquivo, valida campos no backend, retorna feedback claro ao usuário.
- Observações
  - Pode evoluir para relatório por linha/coluna no front.

### C3) Coleta automática de cotações (API)
- Onde
  - Backend: serviço/adaptador para normalizar moedas nos cálculos (margem/receita), com cache e fallback.
- O que faz
  - Busca taxa, aplica normalização de valores multi-moeda.
- Observações
  - Recomendações: cache com TTL, retry/backoff, circuit breaker, uso de env vars para chaves e agendamento diário.

### D1) Refatoração para melhor organização
- Onde
  - Camadas: controllers finos, regras em `services`, adapters/repos isolando I/O.
  - JS organizado por responsabilidade (funções por gráfico/tabela).
- O que faz
  - Reduz acoplamento, facilita testes e manutenção.

### D2) Type hints nas funções principais
- Onde
  - Backend com anotações de tipo nas funções-chave (services/controllers).
- O que faz
  - Melhora leitura, autocompletar e segurança em refactors (possível integração com mypy/CI).

---