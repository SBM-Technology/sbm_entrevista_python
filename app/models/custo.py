"""
Model de Custo.
"""
from datetime import datetime
from app import db


class Custo(db.Model):
    """Representa o custo de um produto."""
    
    __tablename__ = 'custos'
    
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100), nullable=False, unique=True, index=True)
    categoria = db.Column(db.String(50), nullable=False)
    custo_unitario = db.Column(db.Float, nullable=False)
    data_atualizacao = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Custo {self.produto}: R$ {self.custo_unitario}>'
    
    def to_dict(self):
        """Serializa para dicionário."""
        return {
            'id': self.id,
            'produto': self.produto,
            'categoria': self.categoria,
            'custo_unitario': self.custo_unitario,
            'data_atualizacao': self.data_atualizacao.isoformat() if self.data_atualizacao else None
        }

