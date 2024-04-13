import requests
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/api/zelda")
def get_zelda_games():
    url_original = "https://zelda.fanapis.com/api/games"
    respuesta = requests.get(url_original)
    data = json.loads(respuesta.content)
    return jsonify(data)

@app.route("/juegos_zelda")
def zelda_games():
    url_original = "https://zelda.fanapis.com/api/games"
    respuesta = requests.get(url_original)
    data = json.loads(respuesta.content)
    return render_template('juegos_zelda.html', datos=data)

if __name__ == "__main__":
    app.run()
