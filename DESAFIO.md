# 🎯 Desafio: Dashboard Analítico - Python Pleno

## 📋 Sobre o Desafio

Este é um teste prático para **desenvolvedores Python Pleno** focado em:

### 🎯 Competências Avaliadas

**1. Python e Manipulação de Dados (Principal)**
- Processamento eficiente de dados com pandas
- Agregações e transformações complexas
- Validação e limpeza de dados
- ETL (Extract, Transform, Load)
- Queries otimizadas

**2. Visualização de Dados (Principal)**
- Criação de dashboards interativos
- Escolha adequada de gráficos
- Interface intuitiva e responsiva
- Apresentação clara de informações

**3. Flask e Arquitetura (Secundário)**
- Estruturação de projeto
- Boas práticas Python
- Integração com APIs
- Organização do código

---

## ⏱️ Tempo Estimado

**6-10 horas** (pode ser feito em etapas)

---

## 🏁 O Que Já Está Pronto

Para facilitar, este repositório JÁ possui:

✅ **Estrutura Flask completa** (blueprints, models, services)  
✅ **Banco de dados populado** (1.320 registros)  
✅ **Frontend básico** (Bootstrap + Chart.js)  
✅ **4 gráficos funcionando** (linha, barras, pizza, horizontal)  
✅ **Filtros de data** implementados  
✅ **APIs públicas** configuradas (AwesomeAPI, Brasil API)  

**Você pode:**
- ✅ Usar como está e apenas adicionar features
- ✅ Melhorar o que já existe
- ✅ Refatorar e reorganizar
- ✅ Adicionar novas análises

---

## 🎯 O Que Você Deve Fazer

Escolha **pelo menos 3 itens** de cada categoria:

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

## 📊 Tarefas do Desafio

### Categoria A: Manipulação e Análise de Dados (Escolha 3+)

- [ ] **A1:** Calcular margem de lucro (vendas - custos) e exibir no dashboard
- [ ] **A2:** Implementar comparação com metas (% atingido por categoria/região)
- [ ] **A3:** Criar análise de tendências (crescimento mês a mês)
- [ ] **A4:** Adicionar média móvel de vendas (7 dias e 30 dias)
- [ ] **A5:** Implementar ranking de vendedores com métricas de performance
- [ ] **A6:** Criar análise de sazonalidade (vendas por dia da semana)
- [ ] **A7:** Adicionar análise de correlação (vendas × cotação do dólar)
- [ ] **A8:** Implementar cálculo de desvio padrão e outliers

### Categoria B: Visualizações e Dashboard (Escolha 3+)

- [ ] **B1:** Adicionar novo gráfico de desempenho por vendedor
- [ ] **B2:** Criar heatmap de vendas (hora do dia × dia da semana)
- [ ] **B3:** Implementar gráfico de funil de vendas por categoria
- [ ] **B4:** Adicionar gráfico de linha comparando múltiplos períodos
- [ ] **B5:** Criar tabela interativa com ordenação e busca
- [ ] **B6:** Adicionar drill-down (clicar em categoria para ver produtos)
- [ ] **B7:** Implementar gráfico de área (área empilhada de categorias)
- [ ] **B8:** Melhorar responsividade mobile

### Categoria C: Integrações e Funcionalidades (Escolha 2+)

- [ ] **C1:** Melhorar validação do upload de CSV (validar todos os campos)
- [ ] **C2:** Adicionar exportação de relatório em PDF
- [ ] **C3:** Implementar coleta automática de cotações (via API)
- [ ] **C4:** Criar sistema de alertas (quando vendas < meta)
- [ ] **C5:** Adicionar filtros avançados (múltipla seleção de categorias)
- [ ] **C6:** Implementar cache Redis para otimizar consultas
- [ ] **C7:** Criar histórico de uploads com status e logs

### Categoria D: Código e Qualidade (Escolha 2+)

- [ ] **D1:** Refatorar código existente para melhor organização
- [ ] **D2:** Adicionar type hints em todas as funções principais
- [ ] **D3:** Documentar funções com docstrings detalhadas
- [ ] **D4:** Otimizar queries do banco de dados (índices, joins)
- [ ] **D5:** Implementar tratamento de erros robusto
- [ ] **D6:** Adicionar logging apropriado
- [ ] **D7:** Criar documentação de API (endpoints)

---

## ✅ Mínimo Esperado

Para considerar o desafio completo, você deve:

✅ Escolher e implementar **pelo menos 10 itens** no total  
✅ Incluir pelo menos **3 da Categoria A** (Dados)  
✅ Incluir pelo menos **3 da Categoria B** (Visualização)  
✅ Dashboard funcional e responsivo  
✅ Código organizado com boas práticas Python  
✅ README atualizado com suas alterações  

---

## 🌟 Extras (Não obrigatório, mas valorizado)

- ⭐ Análises estatísticas avançadas (correlações, regressão)
- ⭐ Visualizações criativas e informativas
- ⭐ Performance otimizada (cache, queries eficientes)
- ⭐ Interface bonita e intuitiva
- ⭐ Documentação clara e detalhada
- ⭐ Testes unitários (opcional)

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

### Qualidade do Código
- [ ] Code limpo e organizado
- [ ] Boas práticas Python (PEP 8)
- [ ] Type hints nas funções principais
- [ ] Docstrings explicativas
- [ ] Tratamento de erros apropriado

*Nota: Testes unitários são opcionais - foque em funcionalidade e qualidade*

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

### 1. Python e Manipulação de Dados (40%)

**O que vamos avaliar:**
- ✅ Domínio de pandas e manipulação de dados
- ✅ Agregações e transformações eficientes
- ✅ Validação e limpeza de dados
- ✅ ETL bem estruturado
- ✅ Queries otimizadas no banco
- ✅ Tratamento de casos edge e erros

**Como demonstrar:**
- Implemente cálculos complexos (margem, crescimento, médias)
- Faça joins e agregações de múltiplas tabelas
- Trate dados inconsistentes e faltantes
- Otimize processamento de grandes volumes

### 2. Visualização e Dashboard (30%)

**O que vamos avaliar:**
- ✅ Escolha apropriada de gráficos
- ✅ Clareza na apresentação de informações
- ✅ Interface intuitiva e responsiva
- ✅ Interatividade (filtros, drill-down)
- ✅ Design pensado (cores, layout, UX)

**Como demonstrar:**
- Adicione gráficos informativos e bem formatados
- Implemente filtros que funcionem bem
- Crie uma interface agradável de usar
- Pense na experiência do usuário

### 3. Código e Arquitetura (20%)

**O que vamos avaliar:**
- ✅ Organização e estrutura do código
- ✅ Boas práticas Python (PEP 8)
- ✅ Type hints e docstrings
- ✅ Separação de responsabilidades
- ✅ Código limpo e legível

**Como demonstrar:**
- Mantenha código organizado em services/models
- Use type hints nas funções importantes
- Adicione docstrings explicativas
- Siga convenções Python

### 4. Funcionalidade (10%)

**O que vamos avaliar:**
- ✅ Features funcionando corretamente
- ✅ Integração com APIs
- ✅ Upload e processamento de arquivos
- ✅ Sistema rodando sem erros

**Como demonstrar:**
- Implemente features que funcionem bem
- Teste antes de entregar
- Trate erros apropriadamente

---

## 🌟 Diferenciais (Bônus)

Itens que fazem você se destacar:

⭐ **Análises Avançadas:** Correlações, tendências, previsões  
⭐ **Visualizações Criativas:** Gráficos únicos e informativos  
⭐ **Performance:** Cache, otimizações, queries eficientes  
⭐ **UX Excepcional:** Interface muito bem pensada  
⭐ **Documentação:** README detalhado, código bem documentado  
⭐ **Extras:** Features além do solicitado  

---

## ❌ Não é Necessário

Para focar no essencial, você **NÃO precisa**:

❌ Criar testes unitários (opcional)  
❌ Deploy em produção  
❌ Autenticação de usuários  
❌ CI/CD  
❌ Docker (a menos que queira)  
❌ Frontend framework (React, Vue, etc.)

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
