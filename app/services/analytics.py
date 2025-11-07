"""
Serviço de análises e agregações.
"""
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import func, extract
from app import db
from app.models import Venda, Custo, Meta, Cotacao


class Analytics:
    """Realiza análises estatísticas e agregações."""
    
    def calcular_kpis(self, data_inicio=None, data_fim=None):
        """
        Calcula KPIs principais.
        
        Args:
            data_inicio: Data inicial (string YYYY-MM-DD)
            data_fim: Data final (string YYYY-MM-DD)
            
        Returns:
            dict: KPIs calculados
        """
        query = db.session.query(
            func.sum(Venda.valor_total).label('receita_total'),
            func.count(Venda.id).label('num_vendas'),
            func.avg(Venda.valor_total).label('ticket_medio')
        )
        
        query = self._aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        resultado = query.first()
        
        return {
            'receita_total': float(resultado.receita_total or 0),
            'num_vendas': int(resultado.num_vendas or 0),
            'ticket_medio': float(resultado.ticket_medio or 0)
        }
    
    def pvendas_ao_longo_tempo(self, data_inicio=None, data_fim=None):
        """
        Retorna série temporal de vendas.
        
        Returns:
            dict: Dados para gráfico de linhas
        """
        query = db.session.query(
            Venda.data,
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        
        query = self._aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.data).order_by(Venda.data)
        
        resultados = query.all()
        
        return {
            'labels': [r.data.strftime('%Y-%m-%d') for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'quantidades': [int(r.quantidade) for r in resultados]
        }
    
    def vendas_por_categoria(self, data_inicio=None, data_fim=None):
        """
        Retorna vendas agregadas por categoria.
        
        Returns:
            dict: Dados para gráfico de barras
        """
        query = db.session.query(
            Venda.categoria,
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        
        query = self._aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.categoria).order_by(func.sum(Venda.valor_total).desc())
        
        resultados = query.all()
        
        return {
            'labels': [r.categoria for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'quantidades': [int(r.quantidade) for r in resultados]
        }
    
    def vendas_por_regiao(self, data_inicio=None, data_fim=None):
        """
        Retorna vendas agregadas por região.
        
        Returns:
            dict: Dados para gráfico de pizza
        """
        query = db.session.query(
            Venda.regiao,
            func.sum(Venda.valor_total).label('valor')
        )
        
        query = self._aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.regiao).order_by(func.sum(Venda.valor_total).desc())
        
        resultados = query.all()
        total = sum(r.valor for r in resultados)
        
        return {
            'labels': [r.regiao for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'percentuais': [round((r.valor / total * 100), 2) if total > 0 else 0 for r in resultados]
        }
    
    def top_produtos(self, data_inicio=None, data_fim=None, limite=10):
        """
        Retorna top produtos mais vendidos.
        
        Args:
            limite: Número de produtos a retornar
            
        Returns:
            dict: Dados para gráfico de barras horizontal
        """
        query = db.session.query(
            Venda.produto,
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        
        query = self._aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.produto).order_by(func.sum(Venda.valor_total).desc()).limit(limite)
        
        resultados = query.all()
        
        return {
            'labels': [r.produto for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'quantidades': [int(r.quantidade) for r in resultados]
        }
    
    def _aplicar_filtro_data(self, query, model, data_inicio=None, data_fim=None):
        """Aplica filtros de data na query."""
        if data_inicio:
            try:
                dt_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
                query = query.filter(model.data >= dt_inicio)
            except ValueError:
                pass
        
        if data_fim:
            try:
                dt_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
                query = query.filter(model.data <= dt_fim)
            except ValueError:
                pass
        
        return query

