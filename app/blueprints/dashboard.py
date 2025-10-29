"""
Blueprint do dashboard principal.
"""
from flask import Blueprint, render_template, request, jsonify
from app.services.data_processor import DataProcessor
from app.services.analytics import Analytics

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
def index():
    """Página principal do dashboard."""
    return render_template('dashboard/index.html')


@dashboard_bp.route('/data/kpis')
def get_kpis():
    """
    Retorna KPIs principais para o dashboard.
    
    Query params:
        - data_inicio: Data inicial (YYYY-MM-DD)
        - data_fim: Data final (YYYY-MM-DD)
    """
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')
    
    analytics = Analytics()
    kpis = analytics.calcular_kpis(data_inicio, data_fim)
    
    return jsonify(kpis)


@dashboard_bp.route('/data/vendas-tempo')
def get_vendas_tempo():
    """Retorna série temporal de vendas."""
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')
    
    analytics = Analytics()
    dados = analytics.vendas_ao_longo_tempo(data_inicio, data_fim)
    
    return jsonify(dados)


@dashboard_bp.route('/data/vendas-categoria')
def get_vendas_categoria():
    """Retorna vendas por categoria."""
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')
    
    analytics = Analytics()
    dados = analytics.vendas_por_categoria(data_inicio, data_fim)
    
    return jsonify(dados)


@dashboard_bp.route('/data/vendas-regiao')
def get_vendas_regiao():
    """Retorna vendas por região."""
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')
    
    analytics = Analytics()
    dados = analytics.vendas_por_regiao(data_inicio, data_fim)
    
    return jsonify(dados)


@dashboard_bp.route('/data/top-produtos')
def get_top_produtos():
    """Retorna top produtos mais vendidos."""
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')
    limite = request.args.get('limite', 10, type=int)
    
    analytics = Analytics()
    dados = analytics.top_produtos(data_inicio, data_fim, limite)
    
    return jsonify(dados)

