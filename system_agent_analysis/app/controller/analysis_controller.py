from flask import jsonify, request

from app.controller import app
from app.services.analysis_service import analyze_code

@app.route('/analyze_code', methods=['POST'])
def analyze_code_endpoint():
    code = request.json.get('code')
    if not code:
        return jsonify({'error': 'Nessun codice fornito'}), 400

    analysis_result = analyze_code(code)
    return jsonify({'analysis_result': analysis_result})