#!/usr/bin/python3
'''
contains status and stats routes
'''

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
    return jsonify(amenities=storage.count('Amenity'),
                   cites=storage.count('City'),
                   places=storage.count('Place'),
                   reviews=storage.count('Review'),
                   states=storage.count('State'),
                   users=storage.count('User')
                   )
