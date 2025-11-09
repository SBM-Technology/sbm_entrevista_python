import math
from this import d

def test_kpis_ok(client):
    resp = client.get('/data/kpis')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['receita_total', 'num_vendas', 'ticket_medio']:
        assert key in data


def test_vendas_tempo_ok(client):
    resp = client.get('/data/vendas-tempo')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['labels', 'valores', 'quantidades', 'media_movel_7', 'media_movel_30']:
        assert key in data
    # tamanhos coerentes
    n = len(data['labels'])
    assert len(data['valores']) == n
    assert len(data['quantidades']) == n
    assert len(data['media_movel_7']) == n
    assert len(data['media_movel_30']) == n


def test_vendas_categoria_ok(client):
    resp = client.get('/data/vendas-categoria')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['labels', 'valores']:
        assert key in data


def test_vendas_regiao_ok(client):
    resp = client.get('/data/vendas-regiao')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['labels', 'valores', 'percentuais']:
        assert key in data
    # percentuais somam ~100 quando há dados
    if data['percentuais']:
        total = sum(data['percentuais'])
        assert 98 <= total <= 102  # tolerância


def test_top_produtos_ok(client):
    resp = client.get('/data/top-produtos?limite=5')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['labels', 'valores', 'quantidades']:
        assert key in data


def test_vendas_margem_lucro_ordenado_por_margem(client):
    resp = client.get('/data/vendas-margem-lucro')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['labels', 'lucro', 'receita', 'margem']:
        assert key in data
    # verificar ordenação desc por margem
    margem = data['margem']
    if len(margem) >= 2:
        assert margem == sorted(margem, reverse=True)


def test_vendas_dia_semana_labels_ordem(client):
    resp = client.get('/data/vendas-dia-semana')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['labels'] == ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
    for key in ['valores', 'quantidades']:
        assert key in data


def test_vendas_desempenho_por_vendedor(client):
    resp = client.get('/data/vendas-vendedor')
    assert resp.status_code == 200
    data = resp.get_json()
    for key in ['labels', 'valores', 'quantidades', 'ticket_medio', 'percentual_receita', 'ranking']:
        assert key in data
    # verificar ordenação desc por receita
    receita = data['valores']
    if len(receita) >= 2:
        assert receita == sorted(receita, reverse=True)
    # verificar percentuais somam ~100 quando há dados
    if data['percentual_receita']:
        total = sum(data['percentual_receita'])
        assert 98 <= total <= 102  # tolerância
    