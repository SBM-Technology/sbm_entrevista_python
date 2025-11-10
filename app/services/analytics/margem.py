from typing import Dict, Any
from sqlalchemy import func
from app import db
from app.models import Venda, Custo
from .utils import aplicar_filtro_data

class Margem:
    
    def calcular_margem_lucro(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """Retorna a margem de lucro entre as Vendas"""
        query = db.session.query(
            Venda.produto,
            func.sum((Venda.preco_unitario - Custo.custo_unitario) * Venda.quantidade).label("lucro"),
            func.sum(Venda.preco_unitario * Venda.quantidade).label("receita")
        )
        query = query.join(Custo, Venda.produto == Custo.produto)
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.produto)

        #ordernar por margem (lucro/receita) descrecente
        query = query.order_by(
            (func.sum((Venda.preco_unitario - Custo.custo_unitario) * Venda.quantidade) /
            func.nullif(func.sum(Venda.preco_unitario * Venda.quantidade), 0)
            ).desc()
        )
        resultados = query.all()

        return {
            'labels': [r.produto for r in resultados],
            'lucro': [float(r.lucro)  for r in resultados],
            'receita': [float(r.receita) for r in resultados],
            'margem': [float(r.lucro) / float(r.receita) * 100 if r.receita else 0 for r in resultados ]
        }