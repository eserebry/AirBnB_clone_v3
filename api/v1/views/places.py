#!/usr/bin/python3
'''
all place routes
'''

from models import storage, Place, City, State, Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request
from api.v1.views.cities import cities_of_a_state
from functools import reduce


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=['GET', 'POST'])
def places_of_a_city(city_id):
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
        storage.save()
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


def places_city(city_id):
    '''
        helper for search places
    '''
    return [place.to_dict() for place in storage.all('Place').values()
            if place.city_id == city_id]


def place_has_amenities(place, needed_amenities):
    '''
        helper for search places
    '''
    for amenity in needed_amenities:
        if storage.get('Amenity', amenity) not in place.amenities:
            return False
    return True


def place_to_dict(place):
    '''
        helper for search places
    '''
    cp_dct = dict(place.__dict__)
    cp_dct['__class__'] = place.__class__.__name__
    cp_dct['updated_at'] = place.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
    cp_dct['created_at'] = place.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
    if hasattr(place, "_sa_instance_state"):
        del cp_dct["_sa_instance_state"]
    if 'password' in cp_dct.keys():
        if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
            cp_dct.pop('password')
    if 'amenities' in cp_dct.keys():
        cp_dct.pop('amenities')
    return (cp_dct)


@app_views.route('/places_search', strict_slashes=False, methods=['POST'])
def search_places():
    '''
        finds all places with city, state, and amenity constraints
    '''
    search_dict = request.get_json()
    if search_dict is None:
        return 'Not a JSON', 400
    if len(search_dict) == 0:
        all_places = [place.to_dict() for place in storage.all('Places')]
        return jsonify(all_places)
    city_ids = []
    if 'cities' in search_dict.keys():
        city_ids = search_dict['cities']
    if 'states' in search_dict.keys():
        city_ids += reduce((lambda x, y: x + y),
                           [[city.id for city in storage.get('State',
                                                             state_id).cities]
                            for state_id in search_dict['states']])
    place_dicts = reduce((lambda x, y: x + y),
                         [places_city(city_id) for city_id in city_ids])
    places_from_cities = [storage.get('Place',
                                      place['id']) for place in place_dicts]
    str_1 = str(places_from_cities)
    if 'amenities' in search_dict.keys():
        needed_amenities = search_dict['amenities']
        places_with_amenities = [place for place in places_from_cities if
                                 place_has_amenities(place, needed_amenities)
                                 is True]
        all_places = [place_to_dict(place) for place in places_with_amenities]
    else:
        all_places = [place.to_dict() for place in places_from_cities]
    return jsonify(all_places)
