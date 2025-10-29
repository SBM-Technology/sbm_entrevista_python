# 📚 APIs Públicas e Datasets - Referências

Este documento contém informações detalhadas sobre as APIs públicas e datasets que podem ser usados no desafio.

---

## 🌐 APIs Públicas Brasileiras

### 1. AwesomeAPI - Cotações de Moedas

**URL Base:** `https://economia.awesomeapi.com.br`

**Documentação:** https://docs.awesomeapi.com.br/api-de-moedas

#### Endpoints Principais

**1.1 Cotação Atual de Múltiplas Moedas**
```
GET /last/{moedas}

Exemplo:
GET https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL

Retorna:
{
  "USDBRL": {
    "code": "USD",
    "codein": "BRL",
    "name": "Dólar Americano/Real Brasileiro",
    "high": "5.4321",
    "low": "5.3876",
    "varBid": "0.0123",
    "pctChange": "0.23",
    "bid": "5.4123",
    "ask": "5.4156",
    "timestamp": "1234567890",
    "create_date": "2024-01-15 10:30:45"
  },
  "EURBRL": { ... }
}
```

**1.2 Histórico de Cotações (Últimos N Dias)**
```
GET /json/daily/{moeda}-{moeda_destino}/{dias}

Exemplo:
GET https://economia.awesomeapi.com.br/json/daily/USD-BRL/30

Retorna array com histórico dos últimos 30 dias:
[
  {
    "code": "USD",
    "codein": "BRL",
    "name": "Dólar Americano/Real Brasileiro",
    "high": "5.4321",
    "low": "5.3876",
    "varBid": "0.0123",
    "pctChange": "0.23",
    "bid": "5.4123",
    "ask": "5.4156",
    "timestamp": "1234567890",
    "create_date": "2024-01-15"
  },
  ...
]
```

**1.3 Cotação de uma Moeda Específica**
```
GET /json/last/{moeda}-{moeda_destino}

Exemplo:
GET https://economia.awesomeapi.com.br/json/last/USD-BRL
```

#### Moedas Disponíveis
- **USD** - Dólar Americano
- **EUR** - Euro
- **GBP** - Libra Esterlina
- **ARS** - Peso Argentino
- **CAD** - Dólar Canadense
- **AUD** - Dólar Australiano
- **JPY** - Iene Japonês
- **CNY** - Yuan Chinês
- **BTC** - Bitcoin

#### Exemplo de Uso em Python
```python
import requests

# Cotação atual
response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
data = response.json()

usd_valor = float(data['USDBRL']['bid'])
print(f"USD: R$ {usd_valor}")

# Histórico 30 dias
response = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
historico = response.json()

for cotacao in historico:
    print(f"{cotacao['create_date']}: R$ {cotacao['bid']}")
```

#### Limites e Considerações
- ✅ Sem necessidade de API key
- ✅ Rate limit generoso para uso não-comercial
- ✅ Atualização em tempo real
- ⚠️ Recomenda-se usar cache (5-10 minutos)
- ⚠️ Para uso em produção, verificar termos de uso

---

### 2. Brasil API - Dados Econômicos e Públicos

**URL Base:** `https://brasilapi.com.br/api`

**Documentação:** https://brasilapi.com.br/docs

#### Endpoints Principais

**2.1 Taxas de Juros (SELIC, CDI, etc.)**
```
GET /taxas/v1

Exemplo:
GET https://brasilapi.com.br/api/taxas/v1

Retorna:
[
  {
    "nome": "SELIC",
    "valor": 11.75
  },
  {
    "nome": "CDI",
    "valor": 11.65
  }
]
```

**2.2 Feriados Nacionais**
```
GET /feriados/v1/{ano}

Exemplo:
GET https://brasilapi.com.br/api/feriados/v1/2024

Retorna:
[
  {
    "date": "2024-01-01",
    "name": "Confraternização Universal",
    "type": "national"
  },
  {
    "date": "2024-02-13",
    "name": "Carnaval",
    "type": "national"
  },
  ...
]
```

**2.3 Cotação Bitcoin (em BRL)**
```
GET /cptec/v1/bitcoin

Exemplo:
GET https://brasilapi.com.br/api/cptec/v1/bitcoin
```

**2.4 CEP (Busca de endereços)**
```
GET /cep/v2/{cep}

Exemplo:
GET https://brasilapi.com.br/api/cep/v2/01310100
```

**2.5 Bancos (Lista de bancos brasileiros)**
```
GET /banks/v1

Exemplo:
GET https://brasilapi.com.br/api/banks/v1
```

#### Exemplo de Uso em Python
```python
import requests

# Obter taxas de juros
response = requests.get('https://brasilapi.com.br/api/taxas/v1')
taxas = response.json()

for taxa in taxas:
    print(f"{taxa['nome']}: {taxa['valor']}%")

# Obter feriados do ano
response = requests.get('https://brasilapi.com.br/api/feriados/v1/2024')
feriados = response.json()

for feriado in feriados:
    print(f"{feriado['date']}: {feriado['name']}")
```

#### Limites e Considerações
- ✅ Totalmente gratuita e open source
- ✅ Sem necessidade de autenticação
- ✅ Bem documentada
- ✅ Mantida pela comunidade
- ⚠️ Rate limit: razoável para uso normal
- ⚠️ Usar cache quando possível

---

## 📊 Datasets CSV Públicos

### 1. Kaggle - Datasets Diversos

**URL:** https://www.kaggle.com/datasets

**Datasets Relevantes:**
- [E-commerce Data](https://www.kaggle.com/carrie1/ecommerce-data)
- [Retail Sales Dataset](https://www.kaggle.com/datasets/uttamp/retail-sales-data)
- [Supermarket Sales](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)
- [Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

### 2. Brasil.io - Dados Públicos Brasileiros

**URL:** https://brasil.io/datasets/

**Datasets:**
- COVID-19 no Brasil
- Empresas brasileiras
- Eleições
- Gastos públicos

### 3. Data.gov - Dados Governamentais (US)

**URL:** https://data.gov/

**Formato:** CSV, JSON, XML

### 4. Repositórios GitHub

**Datasets de Exemplo:**
```
# Vendas de supermercado
https://raw.githubusercontent.com/datasets/examples/master/retail-sales.csv

# Dados de exemplo genéricos
https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
```

---

## 💡 Outras APIs Úteis (Opcionais)

### 3. OpenWeatherMap (Clima)
```
URL: https://openweathermap.org/api
Requer: API Key gratuita
Limite: 1000 chamadas/dia (free tier)
```

### 4. IBGE API (Dados do IBGE)
```
URL: https://servicodados.ibge.gov.br/api/docs
Endpoints: Municípios, Estados, Indicadores Econômicos
```

### 5. Alpha Vantage (Ações e Forex)
```
URL: https://www.alphavantage.co/
Requer: API Key gratuita
Limite: 5 chamadas/minuto (free tier)
```

---

## 🔧 Boas Práticas no Uso de APIs

### 1. Implementar Cache
```python
from flask_caching import Cache

cache = Cache()

@cache.cached(timeout=300)  # 5 minutos
def obter_cotacao():
    response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    return response.json()
```

### 2. Tratamento de Erros
```python
import requests
from requests.exceptions import RequestException, Timeout

def coletar_dados_api():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Timeout:
        print("Timeout ao acessar API")
    except RequestException as e:
        print(f"Erro na requisição: {e}")
    return None
```

### 3. Retry com Backoff
```python
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def criar_sessao_com_retry():
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
```

### 4. Respeitar Rate Limits
```python
import time

def fazer_multiplas_requisicoes(urls):
    resultados = []
    for url in urls:
        response = requests.get(url)
        resultados.append(response.json())
        time.sleep(1)  # Aguarda 1 segundo entre requisições
    return resultados
```

---

## 📝 Checklist de Integração

Ao integrar uma API externa:

- [ ] Ler a documentação oficial
- [ ] Verificar se precisa de API key
- [ ] Entender os rate limits
- [ ] Implementar tratamento de erros
- [ ] Adicionar retry logic
- [ ] Implementar cache
- [ ] Logar requisições e erros
- [ ] Testar com dados reais
- [ ] Documentar no código
- [ ] Considerar fallback/mock para testes

---

## 🎯 Recomendações para o Desafio

Para o desafio, recomendamos usar:

1. **AwesomeAPI** (cotações) - Simples, sem autenticação, confiável
2. **Brasil API** (taxas/feriados) - Nacional, bem documentada
3. **CSVs fornecidos** - Dados de vendas e custos locais

Foco deve estar em:
- ✅ Coleta eficiente de dados
- ✅ Tratamento de erros
- ✅ Cache para otimizar performance
- ✅ Integração harmoniosa com o dashboard

Boa sorte! 🚀

