# Pokedex DB

## Como executar o projeto

### 1. Instalar dependências
```bash
pip install pipx
pipx install poetry
poetry install
poetry shell
```
2. Backend:
cd backend
```bash
uvicorn backend.app.main:application --reload
```
Acesse http://localhost:8000/docs para verificar se a API está funcionando.

3. Frontend (em outro terminal):
```bash
cd frontend
flask run
```
Acesse http://localhost:5000 para verificar o frontend.

