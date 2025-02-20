from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Ajuste a URL para o Docker (nome do serviço) ou localhost (local)
API_URL = 'http://pokedex:8000'  # Docker
# API_URL = 'http://localhost:8000'  # Local

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form['name']
    try:
        response = requests.post(f'{API_URL}/pokemons/', json={'name': pokemon_name})
        response.raise_for_status()  # Lança exceção para erros 4xx/5xx
        pokemon_data = response.json()
        return render_template('pokedex.html', pokemon=pokemon_data)
    except requests.exceptions.RequestException as e:
        return f"Erro ao se comunicar com o back-end: {str(e)}"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

@app.route('/pokedex')
def pokedex():
    try:
        response = requests.get(f'{API_URL}/pokemons/')
        response.raise_for_status()
        pokemons = response.json()
    except requests.exceptions.RequestException as e:
        pokemons = []
        print(f"Erro ao obter Pokémons: {e}")
    except Exception as e:
        pokemons = []
        print(f"Ocorreu um erro: {str(e)}")
    return render_template("pokedex.html", pokemons=pokemons)

if __name__ == '__main__':
    # Para rodar no Docker, use 0.0.0.0 e a porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)  # Docker
    # Para rodar localmente, use 127.0.0.1 ou localhost e a porta 5000
    # app.run(debug=True)  # Local