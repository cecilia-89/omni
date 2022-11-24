#!/usr/bin/python3
"""Module places_amenities.py: contains amenity information"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.movie import Movie
from models.actor import Actor
from models import storage



@app_views.route('/movie/<movie_id>/actor/<actor_id>',
                 methods=['POST', 'DELETE'],
                 strict_slashes=False)

def movie_cast(movie_id, actor_id):
    movie = storage.get(Movie, movie_id)
    actor = storage.get(Actor, actor_id)

    if movie is None or actor is None:
        abort(404)

    cast = movie.actors
    if request.method == 'POST':
        if actor in cast:
            return jsonify(actor.to_dict())
        movie.actors.append(actor)
        movie.save()
        return jsonify(actor.to_dict()), 201

    if actor not in cast:
        abort(404)
    movie.actors.remove(cast)
    movie.save()
    return '{}'


