#!/usr/bin/python3
'''
all place routes
'''

from models import storage, Place
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=['GET', 'POST'])
def places_of_a_city(state_id):
    '''
        GET: list all places in a specific city
        POST: add a place to a specific city
    '''
    my_city = storage.get('City', city_id)
    if my_city is None:
        abort(404)
    if request.method == 'POST':
        place_dict = request.get_json()
        if place_dict is None:
            return 'Not a JSON', 400
        if 'user_id' not in place_dict.keys():
            return 'Missing user_id', 400
        if 'name' not in place_dict.keys():
            return 'Missing name', 400
        place_dict['city_id'] = city_id
        try:
            my_place = Place(**place_dict)
            my_place.save()
        except:
            abort(404)
        return jsonify(my_place.to_dict()), 201
    my_places = [place.to_dict() for place in storage.all('Place').values()
                 if place.city_id == city_id]
    return jsonify(my_places)


@app_views.route('/places/<place_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def get_place(place_id):
    '''
        GET: display a specific place
        DELETE: delete a place
        PUT: update a place
    '''
    my_place = storage.get('Place', place_id)
    if my_place is None:
        abort(404)
    if request.method == 'DELETE':
        storage.delete(my_place)
        return jsonify({})
    if request.method == 'PUT':
        place_dict = request.get_json()
        if place_dict is None:
            return 'Not a JSON', 400
        for key, value in place_dict.items():
            if key != 'id' and key != 'created_at' and key != 'updated_at':
                if key != 'user_id' and key != 'city_id':
                    setattr(my_place, key, value)
            my_place.save()
    return jsonify(my_place.to_dict())
