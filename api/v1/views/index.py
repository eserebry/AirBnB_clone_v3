#!/usr/bin/python3

from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    '''
        returns a status
    '''
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
def stats():
    '''
        returns amount of each type
    '''
    return jsonify(amenities=storage.count('amenities'),
                   citites=storage.count('cities'),
                   places=storage.count('places'),
                   reviews=storage.count('reviews'),
                   states=storage.count('states'),
                   users=storage.count('users')
                   )
