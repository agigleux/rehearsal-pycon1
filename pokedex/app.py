from flask import Flask, render_template, redirect, url_for, request
import os
import pokedex.helper as helper

app = Flask(__name__)


@app.route('/')
def index():
    pokemon = [{"id": id, "pokemon_name": pokemon_name, "image_url": image_url} for (id, pokemon_name, image_url, _) in
               helper.fetch_all_pokemons()]
    return render_template('index.html', pokemon=pokemon)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    helper.register_subscriber(email)
    return redirect(url_for('index'))


@app.route('/<pokemon_id>')
def pokemon(pokemon_id):
    try:
        _, pokemon_name, image_url, description  = helper.fetch_pokemon(pokemon_id)
        return render_template('pokemon.html', description = description, sprites=[image_url], name = pokemon_name)
    except Exception as e:
        # TODO: handle exception properly
        return redirect(url_for('index'))


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, port=port, debug=True)
