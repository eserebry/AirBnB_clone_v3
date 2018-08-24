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


class test_States(unittest.TestCase):
    '''
        testing the State
    '''
    def test_list_states(self):
        '''
           testing GET method
        '''
        with app.test_client() as c:
            resp = c.get('api/v1/states/')
            self.assertEqual(resp.status_code, 200)

    def test_create_states(self):
        '''
            tetsting POST method
        '''
        with app.test_client() as c:
            resp = c.post('api/v1/states/',
                          data=json.dumps({"name": "NewYork"}),
                          content_type="application/json")
            self.assertEqual(resp.status_code, 201)
