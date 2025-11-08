import os
import pytest
from app import create_app, db
from app.models import Venda, Custo
from datetime import date

@pytest.fixture(scope='session')
def app():
    app = create_app()
    # Override config for testing
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
        WTF_CSRF_ENABLED=False,
        SERVER_NAME='localhost',
    )
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Seed minimal data
        # Custos
        db.session.add_all([
            Custo(produto='A', categoria='Cat1', custo_unitario=5.0, data_atualizacao=date(2025,1,1)),
            Custo(produto='B', categoria='Cat1', custo_unitario=8.0, data_atualizacao=date(2025,1,1)),
            Custo(produto='C', categoria='Cat2', custo_unitario=2.5, data_atualizacao=date(2025,1,1)),
        ])
        # Vendas
        db.session.add_all([
            Venda(data=date(2025,11,1), produto='A', categoria='Cat1', quantidade=2, preco_unitario=10.0, valor_total=20.0, regiao='Sul', vendedor='Joao'),
            Venda(data=date(2025,11,2), produto='B', categoria='Cat1', quantidade=1, preco_unitario=12.0, valor_total=12.0, regiao='Sudeste', vendedor='Ana'),
            Venda(data=date(2025,11,2), produto='C', categoria='Cat2', quantidade=4, preco_unitario=5.0, valor_total=20.0, regiao='Sul', vendedor='Joao'),
            Venda(data=date(2025,11,3), produto='A', categoria='Cat1', quantidade=3, preco_unitario=10.0, valor_total=30.0, regiao='Nordeste', vendedor='Maria'),
        ])
        db.session.commit()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
