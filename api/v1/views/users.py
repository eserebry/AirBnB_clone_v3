#!/usr/bin/python3

import os
from models import storage, User
from api.v1.views import app_views
from flask import jsonify, abort, request
from flasgger import swag_from


@app_views.route('/users', strict_slashes=False,  methods=['GET', 'POST'])
@swag_from(os.getcwd() + '/api/v1/views/apidoc/users_get.yaml',
           methods=['GET'])
@swag_from(os.getcwd() + '/api/v1/views/apidoc/users_post.yaml',
           methods=['POST'])
def all_users():
    '''
        GET: list all users
        POST: create a new user
    '''
    if request.method == 'POST':
        user_dict = request.get_json()
        if user_dict is None:
            return 'Not a JSON', 400
        if 'email' not in user_dict.keys():
            return 'Missing email', 400
        if 'password' not in user_dict.keys():
            return 'Missing password', 400
        my_user = User(**user_dict)
        my_user.save()
        return jsonify(my_user.to_dict()), 201
    my_users = [user.to_dict() for user in storage.all('User').values()]
    return jsonify(my_users)


@app_views.route('/users/<user_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
@swag_from(os.getcwd() + '/api/v1/views/apidoc/users_user-id_get.yaml',
           methods=['GET'])
@swag_from(os.getcwd() + '/api/v1/views/apidoc/users_user-id_delete.yaml',
           methods=['DELETE'])
@swag_from(os.getcwd() + '/api/v1/views/apidoc/users_user-id_put.yaml',
           methods=['PUT'])
def get_user(user_id):
    '''
        GET: display a specific user
        DELETE: delete a user
        PUT: update a user
    '''
    my_user = storage.get('User', user_id)
    if my_user is None:
        abort(404)
    if request.method == 'DELETE':
        storage.delete(my_user)
        return jsonify({})
    if request.method == 'PUT':
        user_dict = request.get_json()
        if user_dict is None:
            return 'Not a JSON', 400
        for key, value in user_dict.items():
            if key != 'id' and key != 'created_at' and key != 'updated_at':
                if key != 'email':
                    setattr(my_user, key, value)
            my_user.save()
    return jsonify(my_user.to_dict())
