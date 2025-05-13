from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the API',
        'status': 'success'
    })

@main.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({
            'error': 'No data provided',
            'status': 'error'
        }), 400 
    
    return jsonify({
        'message': 'Echo successful',
        'data': data,
        'status': 'success'
    })

@main.route('/api/error-example')
def error_example():
    try:
        # Simulate an error
        raise ValueError("This is a test error")
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500 