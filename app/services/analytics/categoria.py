from sqlalchemy import func
from app import db
from app.models import Venda
from .utils import aplicar_filtro_data


class Categoria:
    
    def calcular_vendas_categoria(self, data_inicio: str | None = None, data_fim: str | None = None):
        """Retorna top vendas por categoria."""
        query = db.session.query(
            Venda.categoria,
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.categoria).order_by(func.sum(Venda.valor_total).desc())
        
        resultados = query.all()
        
        return {
            'labels': [r.categoria for r in resultados],
            'valores': [float(r.valor) for r in resultados],
            'quantidades': [int(r.quantidade) for r in resultados]
        }        
