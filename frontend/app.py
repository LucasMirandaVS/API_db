from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL do back-end
API_URL = 'http://localhost:8000'  # Supondo que o back-end esteja rodando localmente

# Página inicial com o formulário de busca de Pokémon
@app.route('/')
def index():
    return render_template('index.html')

# Rota para buscar um Pokémon
@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form['name']
    try:
        response = requests.post(f'{API_URL}/pokemons/', json={'name': pokemon_name})
        if response.status_code == 200:
            pokemon_data = response.json()
            return render_template('pokedex.html', pokemon=pokemon_data)
        else:
            return f"Pokemon '{pokemon_name}' não encontrado na API."
    except requests.exceptions.RequestException as e:
        return f"Erro ao se comunicar com o back-end: {str(e)}"

# Rota para exibir a Pokédex com todos os Pokémons no banco
@app.route('/pokedex')
def pokedex():
    response = requests.get(f'{API_URL}/pokemons/')
    if response.status_code == 200:
        pokemons = response.json()
        return render_template('pokedex.html', pokemons=pokemons)
    return "Erro ao buscar Pokémons"

if __name__ == '__main__':
    app.run(debug=True)
