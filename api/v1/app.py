#!/usr/bin/python3
'''
Main app file
'''

from models import storage
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from flasgger import Swagger


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False
CORS(app, origins='0.0.0.0')
swagger = Swagger(app)


@app.teardown_appcontext
def close_storage(error):
    '''
        closes out storage
    '''
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    '''
        returns error message with 404 on error
    '''
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(5000), threaded=True)
