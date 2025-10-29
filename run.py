"""
Script simplificado para executar o Dashboard Analítico.
Resolve problemas de reload e database locking.
"""
import os
import sys
from pathlib import Path

# IMPORTANTE: Define o diretório de trabalho para o diretório do script
# Isso garante que os caminhos relativos funcionem corretamente
PROJECT_ROOT = Path(__file__).parent.absolute()
os.chdir(PROJECT_ROOT)
sys.path.insert(0, str(PROJECT_ROOT))

print(f"📂 Diretório de trabalho: {os.getcwd()}")

from app import create_app, db

# Cria aplicação
app = create_app()

# Debug: mostra caminho do banco
db_uri = app.config['SQLALCHEMY_DATABASE_URI']
print(f"📊 Database URI: {db_uri}")

# Extrai caminho do banco
if 'sqlite:///' in db_uri:
    db_path = db_uri.replace('sqlite:///', '')
    print(f"📂 Database path: {db_path}")
    print(f"✓ Arquivo existe: {Path(db_path).exists()}")
    print(f"✓ Diretório existe: {Path(db_path).parent.exists()}")
    
    # Verifica permissões
    if Path(db_path).exists():
        print(f"✓ Pode ler: {os.access(db_path, os.R_OK)}")
        print(f"✓ Pode escrever: {os.access(db_path, os.W_OK)}")

# Inicializa banco de dados
with app.app_context():
    try:
        db.create_all()
        print("✅ Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 Dashboard Analítico - Python Pleno")
    print("=" * 70)
    print("📊 URL: http://localhost:5100")
    print("📊 URL: http://127.0.0.1:5100")
    print("=" * 70)
    print("⚠️  Pressione CTRL+C para parar o servidor")
    print("=" * 70)
    print()
    
    # Executa sem debug mode para evitar problemas de reload
    app.run(
        host='0.0.0.0',
        port=5100,
        debug=False,
        use_reloader=False
    )

