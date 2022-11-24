#!/usr/bin/python3
"""Module __init__.py: create a blueprint"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.actors import *
from api.v1.views.movies import *
from api.v1.views.genres import *
from api.v1.views.movie_actors import *