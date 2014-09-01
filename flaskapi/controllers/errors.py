from flaskapi import app
from flask import jsonify, request


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({'status': error.code, 'message': 'not found: ' + request.url})
    response.status_code = error.code
    return response