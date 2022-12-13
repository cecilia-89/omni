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

    movies = [movie.to_dict() for movie in storage.all(Movie)]
    return jsonify(movies)

@app_views.route('/movie/<movie_id>',
                 methods=['DELETE', 'PUT'],
                 strict_slashes=False)
def delete_movie(movie_id):
    """deletes a movie based on it's id"""
    movie = storage.get(Movie, movie_id)
    if movie is None:
        abort(404)

    if request.method == 'DELETE':
        storage.delete(movie)
        storage.save()
        return "deleted\n"

    if request.method == 'PUT':
        res = request.get_json()
        if res is None:
            abort(400, description='Not a JSON')
        for k, v in res.items():
            if k.endswith('ed_at')== 'id':
                continue
            setattr(movie, k, v)
        movie.save()

    return jsonify(city.to_dict())