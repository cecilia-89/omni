#!/usr/bin/python3
"""Module amenities.py: contains amenities information"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.actor import Actor
from models import storage
from distutils.util import strtobool

@app_views.route('/actor',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def actors():
    """displays and creates an amenity"""
    if request.method == 'POST':
        res = request.get_json()
        if res is None:
            abort(400, description='Not a JSON')

        actor = Actor(**res)
        actor.save()
        return jsonify(actor.to_dict()), 201

    actors = {actor.id: f'{actor.first_name} {actor.last_name}'
	          for actor in storage.all(Actor)}
    return actors
