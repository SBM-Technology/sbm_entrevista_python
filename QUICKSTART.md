# 🚀 Quick Start - Dashboard Analítico

## Início Rápido (5 minutos)

### 1. Instale as Dependências
```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate no Windows

pip install -r requirements.txt
```

### 2. Crie o Diretório do Banco (se necessário)
```bash
mkdir -p instance
```

### 3. Importe os Dados
```bash
python3.11 scripts/import_initial_data.py
```

### 4. Execute a Aplicação
```bash
python3.11 app.py
```

### 5. Acesse o Dashboard
Abra seu navegador em: **http://localhost:5000**

---

## 🎯 O que você verá

✅ Dashboard com 4 KPIs principais  
✅ 4 gráficos interativos (linha, barras, pizza)  
✅ Filtros de período funcionais  
✅ Sistema de upload de CSV  
✅ 1000 vendas pré-carregadas  

---

## 📊 Dados Disponíveis

- **Vendas:** 1000 registros (últimos 12 meses)
- **Produtos:** 20 produtos em 5 categorias
- **Regiões:** Norte, Sul, Leste, Oeste, Centro
- **Custos:** Cadastrados para todos os produtos
- **Metas:** Definidas por categoria/região/mês

---

## 🧪 Testando Upload

1. Clique em "Upload" no menu
2. Selecione `data/csv/vendas.csv` (ou qualquer CSV válido)
3. Escolha tipo "Vendas"
4. Clique em "Upload"
5. Dashboard será atualizado automaticamente

---

## 🌐 Testando APIs Externas

### Coletar cotações manualmente:
```bash
curl -X POST http://localhost:5000/api/cotacoes/atualizar
```

### Ver histórico de uploads:
```bash
curl http://localhost:5000/api/uploads
```

---

## 📖 Documentação Completa

- **Desafio Detalhado:** `DESAFIO.md`
- **README Completo:** `PROJECT_README.md`
- **APIs Públicas:** `docs/API_PUBLICA_REFERENCIAS.md`

---

## 🐛 Problemas Comuns

### Erro ao importar dados
```bash
# Regere os dados de exemplo
python3.11 scripts/generate_sample_data.py
python3.11 scripts/import_initial_data.py
```

### Porta 5000 em uso
```bash
# Use outra porta
python3.11 app.py
# E edite app.py para mudar a porta
```

---

Bom desenvolvimento! 🚀

