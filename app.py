"""
Entry point da aplicação Flask.
"""
from app import create_app, db

app = create_app()


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
    app.run(debug=True, host='0.0.0.0', port=5000)

