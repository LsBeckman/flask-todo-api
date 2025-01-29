from flask_sqlalchemy import SQLAlchemy

# Instancia o banco de dados
db = SQLAlchemy()

# Modelo de Tarefa
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'
