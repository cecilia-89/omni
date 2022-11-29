#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template
from models import storage
from models.actor import Actor
from models.genre import Genre
from models.movie import Movie
import uuid

app = Flask(__name__)
movies = storage.all(Movie)

@app.route('/omni/', strict_slashes=False)
def omni():
    """lists all cities in alphabetical order"""
    action = storage.genre('88a468d3-877e-4657-b4e0-50e1e46ef3fa')
    drama = storage.genre('ded6288a-6e3f-4809-8318-f7d0bae223bc')
    romance = storage.genre('43cb9232-52c6-4e6c-9c84-48c776d1f0f5')
    return render_template("practice.html",
                           movies=movies,
                           action = action,
                           drama = drama,
                           romance = romance,
                           )
@app.route('/omni/<movie_id>', strict_slashes=False)
def omni_movie(movie_id):
    movie = storage.get(Movie, movie_id)
    items = [item for item in movies if movie.id != item.id]

    recommended = [item for item in items
                  if item.genre_id == movie.genre_id]
    return render_template("movie.html",
                            movie=movie,
                            recommended=recommended)





@app.teardown_appcontext
def tear_Down(exception):
    """closes a db session or reload file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)