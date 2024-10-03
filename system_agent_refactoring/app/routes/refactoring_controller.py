from flask import request, jsonify
from app import app
from app.services.refactoring_service import refactoring_code


@app.route('/refactoring', methods=['POST'])
def refactoring_code_controller(token):

    new_code = refactoring_code(token)

    return jsonify({'token': token}), 200

