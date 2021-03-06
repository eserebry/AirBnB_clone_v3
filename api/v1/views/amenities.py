#!/usr/bin/python3
'''
all amenity routes
'''

from os import getcwd
from models import storage, Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request
from flasgger import swag_from


@app_views.route('/amenities', strict_slashes=False,  methods=['GET', 'POST'])
@swag_from(getcwd() + '/api/v1/views/apidoc/amenities_get.yaml',
           methods=['GET'])
@swag_from(getcwd() + '/api/v1/views/apidoc/amenities_post.yaml',
           methods=['POST'])
def all_amenities():
    '''
        GET: list all amenities in storage
        POST: add a new amenity
    '''
    if request.method == 'POST':
        amenity_dict = request.get_json()
        if amenity_dict is None:
            return 'Not a JSON', 400
        if 'name' not in amenity_dict.keys():
            return 'Missing name', 400
        my_amenity = Amenity(**amenity_dict)
        my_amenity.save()
        return jsonify(my_amenity.to_dict()), 201
    my_amn = [amenity.to_dict() for amenity in storage.all('Amenity').values()]
    return jsonify(my_amn)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
@swag_from(getcwd() + '/api/v1/views/apidoc/amenities_amenity-id_get.yaml',
           methods=['GET'])
@swag_from(getcwd() + '/api/v1/views/apidoc/amenities_amenity-id_delete.yaml',
           methods=['DELETE'])
@swag_from(getcwd() + '/api/v1/views/apidoc/amenities_amenity-id_put.yaml',
           methods=['PUT'])
def get_amenity(amenity_id):
    '''
        GET: display a specific amenity
        DELETE: delete a amenity
        PUT: update a amenity
    '''
    my_amenity = storage.get('Amenity', amenity_id)
    if my_amenity is None:
        abort(404)
    if request.method == 'DELETE':
        storage.delete(my_amenity)
        storage.save()
        return jsonify({})
    if request.method == 'PUT':
        amenity_dict = request.get_json()
        if amenity_dict is None:
            return 'Not a JSON', 400
        for key, value in amenity_dict.items():
            if key != 'id' and key != 'created_at' and key != 'updated_at':
                setattr(my_amenity, key, value)
        my_amenity.save()
    return jsonify(my_amenity.to_dict())
