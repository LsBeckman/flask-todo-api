# Flask Todo API

This is a simple RESTful API built with Flask and SQLAlchemy to manage tasks.

## Features:
- Create, read, update, and delete tasks.
- Simple SQLite database for task management.

## Getting Started:

1. Clone this repository.

2. Set up a virtual environment:
   ```bash
   python -m venv venv

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Initialize the database:
```bash
python init_db.py
```
5. Run the app:
```bash
python app.py
```
### API Endpoints:

- `POST /tasks:` Create a new task.
- `GET /tasks:` Get a list of tasks.
- `PUT /tasks/<id>:` Update a task.
- `DELETE /tasks/<id>:` Delete a task.
