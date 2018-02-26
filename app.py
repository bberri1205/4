from flask import Flask, render_template, request
import parse

my_site = Flask(__name__)

@my_site.route('/')
def home():
    return render_template("pokedex.html")

@my_site.route("/result", methods=["GET", "POST"])
def results():
    pokeName = request.form.get("name")
    pokeInfo = parse.find_name(pokeName)
    return render_template("results.html", name = pokeName, img = pokeInfo["img"], type = pokeInfo["type"], id = pokeInfo["id"], avspawns = pokeInfo["avg_spawns"] )

if __name__ == "__main__":
    my_site.debug = True
    my_site.run()
