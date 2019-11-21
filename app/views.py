from app import app
import pandas as pd
from flask_caching import Cache
from flask import render_template


cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/")
@cache.cached(timeout=50)
def accueil():
    return render_template('accueil.html')


@app.route("/Volume/Summary")
@cache.cached(timeout=50)
def volume_sumup():
    tot_down = 2453
    tot_marge = 67524.24
    avg_down_marge = int(tot_marge/tot_down)
    return render_template('volume_summary.html',tot_down=tot_down, tot_marge = tot_marge, avg_down_marge=avg_down_marge)


@app.route("/Downgrade/Clients")
@cache.cached(timeout=50)
def clients_downgrade():
    data = pd.read_csv('app/MOUVEMENTS_201910.csv', sep=';', encoding='latin1')
    data.set_index('NUM_CLIENT', inplace = True) 
    extract = data.sort_values('downgrade_marge', ascending=1).head(5) 
    extract = extract.iloc[:,:7]
    return render_template('clients_down.html',tables=[extract.to_html(classes='downgrade')],
    titles = ['na', 'Top 5 downgrades en marge'])

#TEST AREAS#


@app.route("/jinja")
@cache.cached(timeout=50)
def jinja():
    tot_down = 2453
    tot_marge = 67524.24
    avg_down_marge = int(tot_marge/tot_down)
    print(avg_down_marge)
    return render_template("jinja.html", tot_down=tot_down, tot_marge = tot_marge, avg_down_marge=avg_down_marge)
