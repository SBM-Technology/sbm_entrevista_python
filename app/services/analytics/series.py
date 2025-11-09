from typing import Dict, Any
import pandas as pd
from sqlalchemy import func
from app import db
from app.models import Venda
from .utils import aplicar_filtro_data


class Series:

    def calcular_vendas_ao_longo_tempo(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """Retorna série temporal de vendas e médias móveis."""
        query = db.session.query(
            Venda.data,
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.data).order_by(Venda.data)
        
        resultados = query.all()
        labels = [r.data.strftime('%Y-%m-%d') for r in resultados]
        valores = [float(r.valor) for r in resultados]
        quantidades = [int(r.quantidade) for r in resultados]

        # Médias móveis 7 e 30 dias (linhas quebradas para períodos insuficientes)
        try:
            s = pd.Series(valores, index=pd.to_datetime(labels))
            mm7 = s.rolling(window=7).mean().round(2).tolist()
            mm30 = s.rolling(window=30).mean().round(2).tolist()
        except Exception:
            mm7 = [None] * len(valores)
            mm30 = [None] * len(valores)

        return {
            'labels': labels,
            'valores': valores,
            'quantidades': quantidades,
            'media_movel_7': [float(x) if x == x else None for x in mm7],
            'media_movel_30': [float(x) if x == x else None for x in mm30],
        }

    def calcular_top_produtos(self, data_inicio: str | None = None, data_fim: str | None = None, limite: int = 10) -> Dict[str, Any]:
        """Retorna top produtos mais vendidos."""
        query = db.session.query(
            Venda.produto,
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.produto).order_by(func.sum(Venda.valor_total).desc()).limit(limite)
        
        resultados = query.all()
        
        return {
            'labels': [r.produto for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'quantidades': [int(r.quantidade) for r in resultados]
        }

    def calcular_kpis(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """Retorna KPIs principais."""
        query = db.session.query(
            func.sum(Venda.valor_total).label('receita_total'),
            func.count(Venda.id).label('num_vendas'),
            func.avg(Venda.valor_total).label('ticket_medio')
        )
        
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        resultado = query.first()
        
        return {
            'receita_total': float(resultado.receita_total or 0),
            'num_vendas': int(resultado.num_vendas or 0),
            'ticket_medio': float(resultado.ticket_medio or 0),
        }