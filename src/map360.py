from flask import Flask, render_template
import scrape

app = Flask(__name__)

@app.route('/')
def mapa(coordenada=None):
    coordenadas = scrape.main()
    print (coordenadas)
    return render_template('map.html',coordenadas=coordenadas)