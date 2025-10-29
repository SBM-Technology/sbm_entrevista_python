"""
Configurações da aplicação Flask.
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent


class Config:
    """Configuração base."""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = False
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        f'sqlite:///{BASE_DIR / "instance" / "dashboard.db"}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload
    UPLOAD_FOLDER = BASE_DIR / 'data' / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max
    ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls', 'json'}
    
    # Cache
    CACHE_TYPE = 'SimpleCache'  # Use 'RedisCache' para produção
    CACHE_DEFAULT_TIMEOUT = 300  # 5 minutos
    
    # APIs Externas
    AWESOMEAPI_BASE_URL = 'https://economia.awesomeapi.com.br'
    BRASILAPI_BASE_URL = 'https://brasilapi.com.br/api'
    
    # Scheduler (APScheduler)
    SCHEDULER_API_ENABLED = False
    
    # Data files
    DATA_DIR = BASE_DIR / 'data'
    CSV_DIR = DATA_DIR / 'csv'
    JSON_DIR = DATA_DIR / 'json'


class DevelopmentConfig(Config):
    """Configuração de desenvolvimento."""
    DEBUG = True
    CACHE_TYPE = 'SimpleCache'


class ProductionConfig(Config):
    """Configuração de produção."""
    DEBUG = False
    TESTING = False
    
    # Use Redis em produção
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    CACHE_REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    CACHE_REDIS_DB = int(os.getenv('REDIS_DB', 0))
    
    # Database deve vir de variável de ambiente
    if not os.getenv('DATABASE_URL'):
        raise ValueError("DATABASE_URL deve estar definida em produção")


class TestingConfig(Config):
    """Configuração para testes."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Mapeamento de configurações
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

