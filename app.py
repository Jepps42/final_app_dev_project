# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import favorite_animes


# -- Initialization section --
app = Flask(__name__)



# -- Routes section --
@app.route('/')
@app.route('/anime')
def anime():
    return render_template('index.html')

@app.route('/sendAnimelink', methods=['GET', 'POST'])
def sendAnimelink():
    user_name = request.form["user_name"]
    user_anime = request.form["favorite_animes"]
    print(user_name)
    if request.method == 'POST':
        # pass the dictionary into the anime function
        fav_animes = favorite_animes(user_anime)
        return render_template('results.html', user_name=user_name , user_anime=user_anime, fav_animes=fav_animes)