from typing import Dict, Any
import pandas as pd
from sqlalchemy import func
from app import db
from app.models import Venda
from .utils import aplicar_filtro_data


class Vendedor:
    def calcular_vendas_vendedor(
        self,
        data_inicio: str | None = None,
        data_fim: str | None = None,
        limite: int = 10
    ) -> Dict[str, Any]:

        query = db.session.query(
            Venda.vendedor.label('vendedor'),
            func.sum(Venda.valor_total).label('valor_total'),
            func.sum(Venda.quantidade).label('quantidade')
        )

        query = aplicar_filtro_data(query, Venda, data_inicio, data_fim)
        query = query.group_by(Venda.vendedor).order_by(func.sum(Venda.valor_total).desc())

        resultados = query.all()

        if not resultados:
            return {'labels': [], 'valores': [], 'quantidades': [], 'ticket_medio': [], 'percentual_receita': [], 'ranking': []}

        df = pd.DataFrame(
            [(r.vendedor, float(r.valor_total), int(r.quantidade)) for r in resultados],
            columns=['vendedor', 'valor_total', 'quantidade']
        )
        df['ticket_medio'] = df.apply(lambda row: (row['valor_total'] / row['quantidade']) if row['quantidade'] > 0 else 0.0, axis=1)
        total = df['valor_total'].sum()
        df['percentual_receita'] = (df['valor_total'] / total * 100).round(2) if total > 0 else 0.0
        df = df.sort_values('valor_total', ascending=False).head(limite)
        df['ranking'] = df['valor_total'].rank(method='dense', ascending=False).astype(int)

        return {
            'labels': df['vendedor'].tolist(),
            'valores': df['valor_total'].astype(float).tolist(),
            'quantidades': df['quantidade'].astype(int).tolist(),
            'ticket_medio': df['ticket_medio'].round(2).astype(float).tolist(),
            'percentual_receita': df['percentual_receita'].astype(float).tolist(),
            'ranking': df['ranking'].astype(int).tolist(),
        }

    
