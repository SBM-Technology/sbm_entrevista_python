"""
Model de Venda.
"""
from datetime import datetime
from app import db


class Venda(db.Model):
    """Representa uma venda."""
    
    __tablename__ = 'vendas'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False, index=True)
    produto = db.Column(db.String(100), nullable=False, index=True)
    categoria = db.Column(db.String(50), nullable=False, index=True)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    regiao = db.Column(db.String(50), nullable=False, index=True)
    vendedor = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Venda {self.id}: {self.produto} - R$ {self.valor_total}>'
    
    def to_dict(self):
        """Serializa para dicionário."""
        return {
            'id': self.id,
            'data': self.data.isoformat() if self.data else None,
            'produto': self.produto,
            'categoria': self.categoria,
            'quantidade': self.quantidade,
            'preco_unitario': self.preco_unitario,
            'valor_total': self.valor_total,
            'regiao': self.regiao,
            'vendedor': self.vendedor,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

