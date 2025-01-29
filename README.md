Flask Todo API
Uma API RESTful simples construída com Flask para gerenciar tarefas. Este projeto serve como exemplo de como construir uma API que permite a criação, leitura, atualização e exclusão de tarefas usando Flask, SQLAlchemy e outras ferramentas.

Funcionalidades
Criar uma tarefa
Obter uma lista de tarefas
Atualizar uma tarefa
Excluir uma tarefa
Tecnologias Usadas
Flask: Framework web em Python para construir APIs.
SQLAlchemy: ORM para manipulação do banco de dados.
Flask-RESTful: Extensão do Flask para construção de APIs RESTful.
SQLite: Banco de dados utilizado para persistência de dados (pode ser facilmente alterado para outro banco como MySQL ou PostgreSQL).
Como Rodar o Projeto
Clone o repositório para sua máquina local:

git clone https://github.com/seu-usuario/flask-todo-api.git

Navegue até o diretório do projeto:

cd flask-todo-api

Crie um ambiente virtual e ative-o:

python -m venv venv

No Windows:

venv\Scripts\activate

No Linux/Mac:

source venv/bin/activate

Instale as dependências do projeto:

pip install -r requirements.txt

Inicialize o banco de dados:

python init_db.py

Inicie a aplicação Flask:

python app.py

Acesse a API em http://127.0.0.1:5000/.

Endpoints da API
GET /tasks
Retorna a lista de todas as tarefas.
POST /tasks
Cria uma nova tarefa.
Exemplo de corpo da requisição:
json
Copiar
Editar
{
  "title": "Aprender Flask",
  "description": "Construir uma API RESTful",
  "status": "pending"
}
PUT /tasks/<id>
Atualiza uma tarefa existente.
DELETE /tasks/<id>
Exclui uma tarefa.
Como Contribuir
Fork este repositório.
Crie uma nova branch para suas modificações: git checkout -b minha-nova-funcionalidade.
Faça suas alterações e commit: git commit -am 'Adicionando nova funcionalidade'.
Envie para o repositório remoto: git push origin minha-nova-funcionalidade.
Abra um Pull Request.
