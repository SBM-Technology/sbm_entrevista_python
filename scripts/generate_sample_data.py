"""
Script para gerar dados de exemplo para o desafio.
Gera: vendas.csv, custos.csv, metas.json
"""
import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# Configurações
NUM_VENDAS = 1000
DATA_INICIO = datetime(2024, 1, 1)
DATA_FIM = datetime(2024, 12, 31)

# Dados base
PRODUTOS = [
    # Eletrônicos
    ("Notebook Dell", "Eletrônicos", 2800.00, 2200.00),
    ("Mouse Logitech", "Eletrônicos", 89.90, 45.00),
    ("Teclado Mecânico", "Eletrônicos", 350.00, 180.00),
    ("Fone de Ouvido Bluetooth", "Eletrônicos", 199.90, 120.00),
    ("Webcam HD", "Eletrônicos", 299.00, 150.00),
    
    # Roupas
    ("Camiseta Básica", "Roupas", 49.90, 25.00),
    ("Calça Jeans", "Roupas", 159.90, 80.00),
    ("Tênis Esportivo", "Roupas", 299.00, 150.00),
    ("Jaqueta de Couro", "Roupas", 499.00, 250.00),
    
    # Alimentos
    ("Café Premium 500g", "Alimentos", 32.90, 18.00),
    ("Chocolate Importado", "Alimentos", 25.90, 12.00),
    ("Azeite Extra Virgem", "Alimentos", 45.00, 22.00),
    ("Vinho Tinto", "Alimentos", 89.90, 45.00),
    
    # Livros
    ("Livro de Python", "Livros", 79.90, 40.00),
    ("Romance Bestseller", "Livros", 49.90, 25.00),
    ("Livro de Negócios", "Livros", 65.00, 32.00),
    
    # Casa
    ("Jogo de Panelas", "Casa", 299.00, 150.00),
    ("Aspirador de Pó", "Casa", 399.00, 200.00),
    ("Liquidificador", "Casa", 199.00, 100.00),
    ("Jogo de Toalhas", "Casa", 89.90, 45.00),
]

REGIOES = ["Norte", "Sul", "Leste", "Oeste", "Centro"]

VENDEDORES = [
    "Ana Silva", "Carlos Santos", "Maria Oliveira", 
    "João Pereira", "Patricia Costa", "Ricardo Almeida",
    "Fernanda Lima", "Paulo Rodrigues"
]


def random_date(start, end):
    """Gera uma data aleatória entre start e end."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def gerar_vendas():
    """Gera arquivo vendas.csv com dados aleatórios."""
    print("Gerando vendas.csv...")
    
    vendas = []
    for _ in range(NUM_VENDAS):
        produto_info = random.choice(PRODUTOS)
        produto, categoria, preco, _ = produto_info
        
        # Adiciona variação de ±10% no preço
        preco_com_variacao = preco * random.uniform(0.9, 1.1)
        
        venda = {
            "data": random_date(DATA_INICIO, DATA_FIM).strftime("%Y-%m-%d"),
            "produto": produto,
            "categoria": categoria,
            "quantidade": random.randint(1, 10),
            "preco_unitario": round(preco_com_variacao, 2),
            "regiao": random.choice(REGIOES),
            "vendedor": random.choice(VENDEDORES)
        }
        vendas.append(venda)
    
    # Ordena por data
    vendas.sort(key=lambda x: x["data"])
    
    # Salva CSV
    csv_path = Path(__file__).parent.parent / "data" / "csv" / "vendas.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=vendas[0].keys())
        writer.writeheader()
        writer.writerows(vendas)
    
    print(f"✓ Gerado {len(vendas)} registros em {csv_path}")


def gerar_custos():
    """Gera arquivo custos.csv."""
    print("Gerando custos.csv...")
    
    custos = []
    for produto, categoria, _, custo in PRODUTOS:
        custos.append({
            "produto": produto,
            "categoria": categoria,
            "custo_unitario": round(custo, 2),
            "data_atualizacao": "2024-01-01"
        })
    
    csv_path = Path(__file__).parent.parent / "data" / "csv" / "custos.csv"
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=custos[0].keys())
        writer.writeheader()
        writer.writerows(custos)
    
    print(f"✓ Gerado {len(custos)} registros em {csv_path}")


def gerar_metas():
    """Gera arquivo metas.json."""
    print("Gerando metas.json...")
    
    categorias = list(set([cat for _, cat, _, _ in PRODUTOS]))
    
    metas = []
    for ano in [2024]:
        for mes in range(1, 13):
            for categoria in categorias:
                for regiao in REGIOES:
                    # Metas variam por categoria
                    if categoria == "Eletrônicos":
                        meta_base = random.randint(50000, 100000)
                    elif categoria == "Roupas":
                        meta_base = random.randint(30000, 60000)
                    elif categoria == "Casa":
                        meta_base = random.randint(20000, 50000)
                    elif categoria == "Livros":
                        meta_base = random.randint(10000, 30000)
                    else:  # Alimentos
                        meta_base = random.randint(15000, 40000)
                    
                    metas.append({
                        "ano": ano,
                        "mes": mes,
                        "categoria": categoria,
                        "regiao": regiao,
                        "meta_valor": meta_base,
                        "meta_quantidade": random.randint(100, 500)
                    })
    
    json_path = Path(__file__).parent.parent / "data" / "json" / "metas.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(metas, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Gerado {len(metas)} metas em {json_path}")


if __name__ == "__main__":
    print("=" * 60)
    print("Gerando dados de exemplo para o desafio")
    print("=" * 60)
    
    gerar_vendas()
    gerar_custos()
    gerar_metas()
    
    print("\n✅ Todos os arquivos foram gerados com sucesso!")
    print("\nArquivos criados:")
    print("  - data/csv/vendas.csv")
    print("  - data/csv/custos.csv")
    print("  - data/json/metas.json")

