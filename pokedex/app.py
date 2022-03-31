from flask import Flask, render_template
import os
import pokedex.helper as helper

app = Flask(__name__)

@app.route('/')
def index():
	pokemon = [{"id":id, "pokemon_name":pokemon_name, "image_url":image_url} for (id, pokemon_name, image_url, _) in helper.fetch_all_pokemons()]
	return render_template('index.html', pokemon=pokemon)

port = int(os.environ.get('PORT', 5000)) 
if __name__ == '__main__':
	app.run(threaded=True, port=port, debug=True)
