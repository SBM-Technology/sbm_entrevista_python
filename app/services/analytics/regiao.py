from typing import Dict, Any
from sqlalchemy import func
from app import db
from app.models import Venda
from .utils import aplicar_filtro_data


class Regiao:

    def calcular_vendas_por_regiao(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """Retorna vendas agregadas por região."""
        query = db.session.query(
            Venda.regiao,
            func.sum(Venda.valor_total).label('valor')
        )
        
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.regiao).order_by(func.sum(Venda.valor_total).desc())
        
        resultados = query.all()
        total = sum(r.valor for r in resultados)
        
        return {
            'labels': [r.regiao for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'percentuais': [round((r.valor / total * 100), 2) if total > 0 else 0 for r in resultados]
        }
