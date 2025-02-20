FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.5.1

RUN poetry install --no-interaction --no-dev

COPY pokedex /app/pokedex

WORKDIR /app/pokedex/app

COPY start_backend.sh /app/start_backend.sh

# Obtém o caminho para o virtualenv do Poetry
RUN poetry env info --path > /tmp/poetry_path

# Lê o caminho do virtualenv do arquivo
ARG POETRY_VIRTUALENV_PATH=/tmp/poetry_path

# Extrai o caminho do virtualenv
RUN export POETRY_VIRTUALENV_PATH=$(cat $POETRY_VIRTUALENV_PATH)

# Adiciona o diretório bin do virtualenv ao PATH
ENV PATH="$POETRY_VIRTUALENV_PATH/bin:$PATH"

# Adiciona o diretório raiz do projeto ao PYTHONPATH
ENV PYTHONPATH /app:$PYTHONPATH  # <--- Linha adicionada

EXPOSE 8000

# Comando corrigido: executa o script start_backend.sh
CMD ["/app/start_backend.sh"]