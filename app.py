"""
Entry point da aplicação Flask.
"""
import os
from app import create_app, db

app = create_app()

# Cria tabelas do banco de dados se não existirem
# (apenas na primeira execução, não no reload do watchdog)
if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
    with app.app_context():
        try:
            db.create_all()
            print("✓ Tabelas do banco de dados verificadas")
        except Exception as e:
            print(f"⚠️  Aviso: {e}")


@app.cli.command()
def init_db():
    """Inicializa o banco de dados."""
    db.create_all()
    print("✓ Banco de dados inicializado!")


@app.cli.command()
def import_data():
    """Importa dados iniciais dos CSVs."""
    from scripts.import_initial_data import main
    main()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)

