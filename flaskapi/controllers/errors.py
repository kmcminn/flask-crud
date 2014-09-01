from flaskapi.util import *
from flaskapi import app
from flask import jsonify, request


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({'status': 404, 'message': 'not found' + request.url})
    response.status_code = 404
    return response