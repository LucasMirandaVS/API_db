#!/bin/bash

# Obtém o caminho para o virtualenv do Poetry (ajuste conforme necessário)
POETRY_VIRTUALENV_PATH=$(poetry env info --path)

# Ativa o ambiente virtual
source $POETRY_VIRTUALENV_PATH/bin/activate

# Executa uvicorn (especifica o módulo dentro do pacote)
exec uvicorn pokedex.app.main:application --host 0.0.0.0 --port 8000