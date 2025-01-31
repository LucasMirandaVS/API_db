from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = 'http://localhost:8000'  # Backend Local

@app.route('/')
def index():
    return render_template('index.html')

# Busca Pokémon específico
@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form['name']
    try:
        response = requests.post(f'{API_URL}/pokemons/', json={'name': pokemon_name})
        if response.status_code == 200:
            pokemon_data = response.json()
            return render_template('pokedex.html', pokemon=pokemon_data)
        else:
            return render_template('pokedex.html', name=pokemon_name)
    except requests.exceptions.RequestException as e:
        return f"Erro ao se comunicar com o back-end: {str(e)}"

# Exibe a Pokédex com todos os Pokémons do banco de dados
@app.route('/pokedex')
def pokedex():
    try:
        response = requests.get(f'{API_URL}/pokemons/')
        if response.status_code == 200:
            pokemons = response.json()
        else:
            pokemons = []
    except requests.exceptions.RequestException:
        pokemons = []
    return render_template("pokedex.html", pokemons=pokemons)

if __name__ == '__main__':
    app.run(debug=True)
