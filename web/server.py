# -*- coding: utf-8 -*-
from flask import Flask, render_template
import sys
import os

# Permet d'importer les modules du dossier parent
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    print("🌐 Serveur DZ-IA OUERD lancé sur http://127.0.0.1:5000")
    app.run(port=5000, debug=True)