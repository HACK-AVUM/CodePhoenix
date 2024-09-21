import jwt
from flask import request, jsonify

from system_agent_doc.app import app
from system_agent_doc.app.services.docs_service import generate_documentation


@app.route('/generate_documentation', methods=['POST'])
def generate_documentation_endpoint():
    code = request.json.get('code')
    if not code:
        return jsonify({'error': 'Nessun codice fornito'}), 400

    documentation = generate_documentation(code)
    return jsonify({'documentation': documentation})