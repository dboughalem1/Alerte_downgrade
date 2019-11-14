from app import app
import pandas as pd
from flask_caching import Cache



cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/")
@cache.cached(timeout=50)
def acceuil():
    #return render_template('Acceuil.html')
     return "hello its working !!!!!"


@app.route("/Summary")
@cache.cached(timeout=50)
def sumup():
    return render_template('Summary.html')
