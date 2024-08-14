from flask import Flask,render_template
from fetchAPIs import fetch_now_playing,fetch_top_rated, fetch_trending, fetch_upcoming
from flask_cors import CORS


app =Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/now_playing')
def nowPlaying():
    return fetch_now_playing()

@app.route('/top_rated')
def topRated():
    return fetch_top_rated()

@app.route('/trending')
def trending():
    return fetch_trending()

@app.route('/upcoming')
def upcoming():
    return fetch_upcoming()

if __name__=='__main__':
    app.run(debug=True)
