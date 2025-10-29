"""
Models da aplicação.
"""
from app.models.venda import Venda
from app.models.custo import Custo
from app.models.cotacao import Cotacao
from app.models.meta import Meta
from app.models.upload import Upload

__all__ = ['Venda', 'Custo', 'Cotacao', 'Meta', 'Upload']

