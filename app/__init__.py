"""
Inicialização da aplicação Flask.
"""
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

# Inicializa extensões
db = SQLAlchemy()
cache = Cache()


def create_app(config_name='default'):
    """
    Factory pattern para criar a aplicação Flask.
    
    Args:
        config_name: Nome da configuração (development, production, testing)
    """
    app = Flask(__name__)
    
    # Carrega configuração
    from config import config
    app.config.from_object(config[config_name])
    
    # Inicializa extensões
    db.init_app(app)
    cache.init_app(app)
    
    # Cria diretórios necessários
    app.config['UPLOAD_FOLDER'].mkdir(parents=True, exist_ok=True)
    
    # Cria diretório instance para o banco de dados SQLite
    from pathlib import Path
    instance_path = Path(app.instance_path)
    instance_path.mkdir(parents=True, exist_ok=True)
    
    # Registra blueprints
    from app.blueprints.dashboard import dashboard_bp
    from app.blueprints.api import api_bp
    
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Scheduler simples para coleta automática de cotações (C3)
    try:
        minutos = int(app.config.get('COTACOES_SCHEDULE_MINUTES', 60))
        if minutos > 0:
            scheduler = BackgroundScheduler(daemon=True)
            def job_coletar_cotacoes():
                with app.app_context():
                    try:
                        from app.services.collectors.data_collector import DataCollector
                        DataCollector().coletar_cotacoes()
                    except Exception as e:
                        app.logger.error(f"Scheduler cotacoes: {e}")
            scheduler.add_job(job_coletar_cotacoes, 'interval', minutes=minutos, id='cotacoes_job', replace_existing=True)
            scheduler.start()
    except Exception as e:
        app.logger.error(f"Falha ao iniciar scheduler: {e}")

    return app

