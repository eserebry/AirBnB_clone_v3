#!/usr/bin/python3
'''
    Testing the State object
'''
import pep8
import unittest
import sys
import json
from api.v1.app import *
from flask import request, jsonify
from models import storage
from models.user import User
from models.state import State


class test_Users(unittest.TestCase):
    '''
        testing the User
    '''
    def test_list_users(self):
        '''
           testing GET method
        '''
        with app.test_client() as c:
            resp = c.get('api/v1/users/')
            self.assertEqual(resp.status_code, 200)

    '''
    def test_create_users(self):
        with app.test_client() as c:
            resp = c.post('api/v1/users/',
                          data=json.dumps({}),
                          content_type="application/json")
            self.assertEqual(resp.status_code, 201)
   '''
