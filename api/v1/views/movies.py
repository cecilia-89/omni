#!/usr/bin/python3
"""Module amenities.py: contains amenities information"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.movie import Movie
from models import storage
from distutils.util import strtobool

@app_views.route('/movie',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def movies():
    """displays and creates an amenity"""
    if request.method == 'POST':
        res = request.get_json()
        res['rated_18'] = strtobool(res['rated_18'])
        res['series'] = strtobool(res['series'])
        if res is None:
            abort(400, description='Not a JSON')

        movie = Movie(**res)
        movie.save()
        return jsonify(movie.to_dict()), 201

    movies = {movie.title:movie.id for movie in storage.all(Movie)}
    return movies
