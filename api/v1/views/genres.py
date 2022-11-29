#!/usr/bin/python3
"""Module amenities.py: contains amenities information"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.genre import Genre
from models import storage
from distutils.util import strtobool

@app_views.route('/genre',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def genre():
    """displays and creates a genre object"""
    if request.method == 'POST':
        res = request.get_json()
        if res is None:
            abort(400, description='Not a JSON')

        genre = Genre(**res)
        print(genre.to_dict())
        genre.save()
        return jsonify(genre.to_dict()), 201

    genres = {genre.id:genre.title for genre in storage.all(Genre)}
    return genres


@app_views.route('/genre/<genre_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_genre(genre_id):
    """displays and creates a genre object"""
    if request.method == 'DELETE':
        genre = storage.get(Genre, genre_id)
        storage.delete(genre)
        storage.save()

    return "deleted\n"