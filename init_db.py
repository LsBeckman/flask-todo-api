from app import app, db

# Função para inicializar o banco de dados
def init_db():
    with app.app_context():  # Cria o contexto de aplicação
        db.create_all()  # Cria as tabelas no banco de dados

# Chama a função para inicializar o banco de dados
init_db()
