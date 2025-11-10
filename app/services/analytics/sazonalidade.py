from typing import Dict, Any
from sqlalchemy import func
from app import db
from app.models import Venda
from .utils import aplicar_filtro_data


class Sazonalidade:

    def calcular_sazonalidade_dia_semana(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """
        Retorna a sazonalidade das vendas por dia da semana
        """
        # strftime('%w') retorna 0..6 onde 0=Domingo no SQLite/Postgres compatível via func
        query = db.session.query(
            func.strftime('%w', Venda.data).label('dow'),
            func.sum(Venda.valor_total).label('valor'),
            func.sum(Venda.quantidade).label('quantidade')
        )
        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by('dow')
        resultados = query.all()

        mapa_dias = {str(i): {'valor': 0.0, 'quantidade': 0} for i in range(7)}
        for r in resultados:
            k = str(r.dow)
            mapa_dias[k] = {
                'valor': float(r.valor or 0),
                'quantidade': int(r.quantidade or 0)
            }

        return {
            'labels': ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
            'valores': [mapa_dias[str(i)]['valor'] for i in range(7)],
            'quantidades': [mapa_dias[str(i)]['quantidade'] for i in range(7)],
        }