from sqlalchemy.orm import Query
from app.models import Venda
from datetime import datetime

def aplicar_filtro_data(query: Query, model: Venda, data_inicio: str | None = None, data_fim: str | None = None) -> Query:
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
