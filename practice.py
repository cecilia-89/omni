#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template
from models import storage
from models.actor import Actor
from models.genre import Genre
from models.movie import Movie
import uuid

app = Flask(__name__)


@app.route('/omni/', strict_slashes=False)
def hbnb():
    """lists all cities in alphabetical order"""
    actors = storage.all(Actor)
    genres = storage.all(Genre)
    movies = storage.all(Movie)
    return render_template("practice.html",
                           actors=actors,
                           genres=genres,
                           movies=movies,
                           cache_id=uuid.uuid4())


@app.teardown_appcontext
def tear_Down(exception):
    """closes a db session or reload file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)