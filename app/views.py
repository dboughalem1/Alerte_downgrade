from app import app
import pandas as pd
from flask_caching import Cache
from flask import render_template


cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/")
@cache.cached(timeout=50)
def accueil():
    return render_template('accueil.html')


@app.route("/Summary")
@cache.cached(timeout=50)
def sumup():
    return render_template('sumup.html')
