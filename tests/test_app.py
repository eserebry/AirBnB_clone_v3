from api.v1.app import app
import unittest


class TestApp(unittest.TestCase):
    '''
        unit testing for api
    '''

    def setUp(self):
        '''
            set-up for unit testing
        '''
        self.app = app.test_client()

    def test_check_status(self):
        '''
            testing status route and api basic functionality
        '''
        rv = self.app.get('/api/v1/status')
        self.assertEqual(rv.data, b'{\n  "status": "OK"\n}\n')
        self.assertEqual(rv._status_code, 200)
        self.assertEqual(rv.headers[0][1], 'application/json')

    def test_not_found(self):
        '''
            testing 404 page
        '''
        rv = self.app.get('/api/v1/nop')
        self.assertEqual(rv.data, b'{\n  "error": "Not found"\n}\n')
        self.assertEqual(rv._status_code, 404)

    def test_state(self):
        '''
            testing states route
        '''
        rv = self.app.get('/api/v1/states')
        self.assertEqual(rv._status_code, 200)
