# 🎯 Desafio: Dashboard Analítico com Múltiplas Fontes de Dados

## 📋 Descrição do Desafio

Você deve desenvolver um **Dashboard Analítico** em Flask que integra dados de múltiplas fontes, realiza análises estatísticas e apresenta visualizações interativas.

O dashboard deve coletar, processar e exibir dados sobre **vendas de produtos e indicadores econômicos**, permitindo análises correlacionadas entre as diferentes fontes de dados.

---

## 🎯 Objetivos

Avaliar suas competências em:
- ✅ Coleta de dados de múltiplas fontes (CSV, APIs, banco de dados)
- ✅ Tratamento e normalização de dados heterogêneos
- ✅ ETL (Extract, Transform, Load)
- ✅ Análise estatística e agregações complexas
- ✅ Visualização de dados com gráficos interativos
- ✅ Arquitetura Flask bem estruturada
- ✅ Performance e otimização

---

## 📊 Fontes de Dados

### 1. **Arquivo CSV - Dados de Vendas**
Localização: `data/csv/vendas.csv`

O arquivo contém dados históricos de vendas com as seguintes colunas:
- `data`: Data da venda (formato: YYYY-MM-DD)
- `produto`: Nome do produto
- `categoria`: Categoria do produto
- `quantidade`: Quantidade vendida
- `preco_unitario`: Preço unitário em BRL
- `regiao`: Região da venda (Norte, Sul, Leste, Oeste, Centro)
- `vendedor`: Nome do vendedor

### 2. **API Pública - Cotações de Moedas**
**API:** [AwesomeAPI - Economia](https://docs.awesomeapi.com.br/api-de-moedas)

**Endpoints úteis:**
```
# Cotação atual USD-BRL
GET https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL

# Cotações dos últimos 30 dias
GET https://economia.awesomeapi.com.br/json/daily/USD-BRL/30

# Documentação completa
https://docs.awesomeapi.com.br/api-de-moedas
```

### 3. **API Pública - Dados Econômicos do Brasil**
**API:** [Brasil API](https://brasilapi.com.br/)

**Endpoints úteis:**
```
# Taxas de juros (SELIC)
GET https://brasilapi.com.br/api/taxas/v1

# IBGE - Feriados nacionais
GET https://brasilapi.com.br/api/feriados/v1/{ano}

# Documentação completa
https://brasilapi.com.br/docs
```

### 4. **Arquivo JSON - Metas de Vendas**
Localização: `data/json/metas.json`

Contém as metas mensais de vendas por categoria e região.

### 5. **CSV Adicional - Custos de Produtos**
Localização: `data/csv/custos.csv`

Contém o custo de cada produto para cálculo de margem de lucro.

---

## 🚀 Funcionalidades Obrigatórias

### 1. **Coleta de Dados**

#### 1.1 Importação de CSV
- [ ] Upload manual de arquivos CSV via interface web
- [ ] Validação de formato e colunas obrigatórias
- [ ] Processamento de arquivos grandes (usar chunks/streaming)
- [ ] Feedback de progresso durante upload
- [ ] Histórico de uploads realizados

#### 1.2 Integração com APIs
- [ ] Consumir API de cotações (AwesomeAPI)
- [ ] Consumir API de taxas (Brasil API)
- [ ] Armazenar histórico de cotações no banco
- [ ] Agendamento de coletas periódicas (opcional: APScheduler)
- [ ] Tratamento de erros e retry
- [ ] Cache de resultados (5-10 minutos)

#### 1.3 Importação de JSON
- [ ] Leitura do arquivo de metas
- [ ] Validação de estrutura
- [ ] Armazenamento no banco de dados

### 2. **Tratamento e Análise de Dados**

#### 2.1 Processamento
- [ ] Normalização de datas (timezone, formato)
- [ ] Validação de dados (valores negativos, campos vazios)
- [ ] Cálculo de valores derivados:
  - Valor total da venda (quantidade × preço_unitario)
  - Margem de lucro (preço - custo)
  - Percentual de lucro
- [ ] Join de dados de diferentes fontes:
  - Vendas + Custos (por produto)
  - Vendas + Metas (por categoria/região/período)
  - Vendas + Cotações (para análise de impacto cambial)

#### 2.2 Agregações
- [ ] Vendas totais por período (dia, semana, mês)
- [ ] Vendas por produto/categoria/região/vendedor
- [ ] Média, máximo, mínimo de vendas
- [ ] Crescimento percentual (comparação com período anterior)
- [ ] Atingimento de metas (percentual)
- [ ] Produtos mais vendidos (top 10)
- [ ] Regiões com melhor desempenho

#### 2.3 Análise Estatística
- [ ] Correlação entre volume de vendas e cotação do dólar
- [ ] Média móvel de vendas (7 dias, 30 dias)
- [ ] Desvio padrão de vendas por produto
- [ ] Identificação de tendências (crescimento/declínio)

### 3. **Visualizações no Dashboard**

#### 3.1 KPIs Principais (Cards no topo)
- [ ] Receita total do período
- [ ] Número de vendas
- [ ] Ticket médio
- [ ] Margem de lucro média
- [ ] Crescimento vs. período anterior (%)

#### 3.2 Gráficos Obrigatórios
1. **Gráfico de Linhas:** Evolução de vendas ao longo do tempo
   - Múltiplas séries (receita, quantidade, cotação dólar)
   - Filtro de período

2. **Gráfico de Barras:** Vendas por categoria
   - Comparação com meta
   - Ordenação por valor

3. **Gráfico de Pizza/Donut:** Distribuição de vendas por região
   - Percentuais
   - Legenda interativa

4. **Gráfico de Barras Horizontal:** Top 10 produtos mais vendidos
   - Ordenado por valor ou quantidade

5. **Heatmap/Tabela:** Desempenho por vendedor × categoria
   - Cores indicando performance

6. **Gráfico de Dispersão:** Correlação entre vendas e cotação do dólar
   - Eixo X: cotação
   - Eixo Y: volume de vendas

#### 3.3 Interatividade
- [ ] Filtros de período (data inicial/final, mês, ano)
- [ ] Filtros por categoria, região, vendedor
- [ ] Todos os gráficos atualizam ao mudar filtros
- [ ] Tooltips informativos nos gráficos
- [ ] Drill-down (clicar em gráfico para detalhar) - opcional

### 4. **Funcionalidades Adicionais**

- [ ] Exportação de relatórios (CSV ou PDF)
- [ ] Tabela de dados com paginação, ordenação e busca
- [ ] Comparação entre períodos (mês anterior, ano anterior)
- [ ] Indicadores visuais (cores) para metas atingidas/não atingidas
- [ ] Responsividade (mobile-friendly)

---

## 🏗️ Requisitos Técnicos

### Arquitetura
- [ ] Estrutura organizada com blueprints
- [ ] Separação de responsabilidades (models, services, routes)
- [ ] Configuração centralizada (config.py ou .env)
- [ ] Factory pattern para criação do app (opcional)

### Banco de Dados
- [ ] SQLAlchemy como ORM
- [ ] Models para: Vendas, Cotações, Metas, Custos, Uploads
- [ ] Relacionamentos apropriados
- [ ] Migrations (Alembic) - opcional
- [ ] Índices em colunas frequentemente consultadas

### Performance
- [ ] Queries otimizadas (evitar N+1)
- [ ] Cache de resultados de APIs externas
- [ ] Paginação em listas grandes
- [ ] Processamento eficiente de CSVs grandes (chunks)

### Código
- [ ] Type hints em funções principais
- [ ] Docstrings em funções/classes
- [ ] Tratamento de exceções adequado
- [ ] Validação de dados de entrada
- [ ] Logging apropriado

### Testes (Opcional, mas valorizado)
- [ ] Testes unitários (pytest)
- [ ] Testes de integração
- [ ] Cobertura mínima de 50%
- [ ] Fixtures para dados de teste

---

## 📦 Stack Tecnológica Sugerida

### Obrigatórias
- **Framework:** Flask 2.x+
- **ORM:** SQLAlchemy
- **Banco de Dados:** SQLite (desenvolvimento) ou PostgreSQL (produção)
- **Processamento:** pandas, numpy
- **HTTP Client:** requests

### Visualização (escolha uma)
- **Chart.js** (recomendado - simples e eficiente)
- **Plotly.js** (mais avançado)
- **D3.js** (máxima flexibilidade)

### Complementares (opcional)
- **Flask-Caching:** Para cache
- **APScheduler:** Para agendamento de tarefas
- **python-dotenv:** Para variáveis de ambiente
- **WTForms:** Para validação de formulários
- **pytest:** Para testes

---

## 📁 Estrutura do Projeto Sugerida

```
sbm_entrevista_python/
├── app/
│   ├── __init__.py
│   ├── blueprints/
│   │   ├── __init__.py
│   │   ├── dashboard.py      # Rotas do dashboard
│   │   └── api.py             # Rotas da API interna
│   ├── models/
│   │   ├── __init__.py
│   │   ├── venda.py
│   │   ├── cotacao.py
│   │   ├── meta.py
│   │   └── custo.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── data_collector.py  # Coleta de APIs
│   │   ├── data_processor.py  # Processamento/ETL
│   │   └── analytics.py       # Análises estatísticas
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── dashboard.js   # Lógica dos gráficos
│   ├── templates/
│   │   ├── layouts/
│   │   │   └── base.html
│   │   ├── dashboard/
│   │   │   └── index.html
│   │   └── components/
│   │       └── filters.html
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── data/
│   ├── csv/
│   │   ├── vendas.csv
│   │   └── custos.csv
│   ├── json/
│   │   └── metas.json
│   └── uploads/               # CSVs enviados pelo usuário
├── tests/
│   ├── __init__.py
│   ├── unit/
│   └── integration/
├── config.py                  # Configurações
├── app.py                     # Entry point
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md                  # Instruções de setup
```

---

## 🗄️ Esquema do Banco de Dados (Sugestão)

### Tabela: vendas
```sql
id, data, produto, categoria, quantidade, preco_unitario, 
regiao, vendedor, valor_total, created_at
```

### Tabela: custos
```sql
id, produto, custo_unitario, data_atualizacao
```

### Tabela: cotacoes
```sql
id, moeda, valor, data_hora, created_at
```

### Tabela: metas
```sql
id, categoria, regiao, mes, ano, meta_valor, meta_quantidade
```

### Tabela: uploads
```sql
id, nome_arquivo, tipo, status, num_registros, created_at
```

---

## 📈 Dados de Exemplo Fornecidos

### vendas.csv
- **Registros:** ~1000 vendas
- **Período:** últimos 12 meses
- **Produtos:** 20 produtos diferentes
- **Categorias:** Eletrônicos, Roupas, Alimentos, Livros, Casa
- **Regiões:** Norte, Sul, Leste, Oeste, Centro

### custos.csv
- Custo de cada um dos 20 produtos

### metas.json
- Metas mensais por categoria e região

---

## ✅ Critérios de Avaliação

### 1. Funcionalidade (40%)
- [ ] Todas as funcionalidades obrigatórias implementadas
- [ ] Sistema funciona sem erros críticos
- [ ] Tratamento adequado de casos edge

### 2. Código e Arquitetura (30%)
- [ ] Estrutura organizada e clara
- [ ] Código limpo e legível
- [ ] Boas práticas Python
- [ ] Separação de responsabilidades
- [ ] Type hints e documentação

### 3. Dados e Análises (20%)
- [ ] ETL bem implementado
- [ ] Análises estatísticas corretas
- [ ] Agregações eficientes
- [ ] Tratamento de dados inconsistentes

### 4. Interface e Visualizações (10%)
- [ ] Gráficos apropriados e informativos
- [ ] Interface intuitiva
- [ ] Responsividade básica
- [ ] Filtros funcionais

### Bônus (+10%)
- [ ] Testes automatizados
- [ ] Cache implementado
- [ ] Agendamento de coletas
- [ ] Documentação completa
- [ ] Deploy configurado (Docker, etc.)

---

## 🚀 Como Começar

### 1. Setup do Ambiente
```bash
# Clone o repositório
git clone <repo-url>
cd sbm_entrevista_python

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env

# Inicialize o banco de dados
python -c "from app import db; db.create_all()"

# Execute a aplicação
python app.py
```

### 2. Importe os Dados Iniciais
```bash
# Rode um script para popular o banco com os CSVs fornecidos
python scripts/import_initial_data.py
```

### 3. Acesse o Dashboard
```
http://localhost:5000
```

---

## 📚 Recursos Úteis

### Documentação de APIs
- [AwesomeAPI - Moedas](https://docs.awesomeapi.com.br/api-de-moedas)
- [Brasil API](https://brasilapi.com.br/docs)

### Datasets Alternativos (caso queira usar outros)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Brasil.io](https://brasil.io/datasets/)
- [Data.gov](https://data.gov/)

### Bibliotecas de Visualização
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [Plotly.js Documentation](https://plotly.com/javascript/)

### Tutoriais Flask
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

---

## ⏱️ Tempo Estimado

**6-12 horas** (dependendo da experiência e escopo)

- Setup e estrutura: 1h
- Models e banco: 1h
- Coleta de dados (CSV + APIs): 2-3h
- Processamento e análises: 2-3h
- Dashboard e visualizações: 3-4h
- Testes e refinamentos: 1-2h

---

## 📝 Entrega

### O que enviar:
1. **Código completo** (repositório Git ou ZIP)
2. **README.md** com:
   - Instruções de setup e execução
   - Decisões técnicas tomadas
   - Dificuldades encontradas
   - Melhorias futuras
3. **requirements.txt** atualizado
4. **Screenshots** ou vídeo demonstrativo (opcional)

### Como será avaliado:
- Code review do código enviado
- Execução local do projeto
- Análise da arquitetura e decisões
- Discussão técnica sobre as escolhas feitas

---

## 💡 Dicas

1. **Comece simples:** Implemente as funcionalidades core primeiro, depois refine
2. **Commits frequentes:** Mostre seu processo de desenvolvimento
3. **Não reinvente a roda:** Use bibliotecas consolidadas
4. **Performance importa:** Mas não otimize prematuramente
5. **README é importante:** Explique suas decisões e como rodar o projeto
6. **Testes valem pontos:** Mesmo que básicos
7. **Pergunte se tiver dúvidas:** Comunicação é importante

---

## 🎯 Boa Sorte!

Mostre suas habilidades técnicas, capacidade de resolver problemas e atenção aos detalhes. Estamos ansiosos para ver sua solução! 🚀
