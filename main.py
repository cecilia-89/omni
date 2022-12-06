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
    """returns variables to practice.html template"""
    movies = storage.all(Movie)
    lists = {item.title:storage.genre(item.id) for item in storage.all(Genre)}
    count = storage.count(Movie)
    return render_template("practice.html",
                           movies=movies[0:5],
                           lists=lists,
                           count=count
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