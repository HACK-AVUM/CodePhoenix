from requests import *
from flask import jsonify


from app.controller import app
from app.services.test_service import perform_test


@app.route('/perform_test', methods=['POST'])
def perform_test_endpoint():

    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'Nessun dato fornito'}), 400

    test_result = perform_test(data)
    return jsonify({'test_result'})