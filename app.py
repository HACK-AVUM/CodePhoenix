from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Import service functions
from system_agent_refactoring.app.services.refactoring_service import refactoring_code
from system_agent_analysis.app.services.analysis_service import analyze_code
from system_agent_test.app.services.test_service import perform_test
from system_agent_scanning_vuln.app.services.scanning_vulnerability_service import perform_scan_vulnerability

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"error": "No code provided"}), 400

    code = data['code']
    analysis_result = analyze_code(code)
    return jsonify({"analysis_result": analysis_result})

@app.route('/refactor', methods=['POST'])
def refactor():
    data = request.get_json()
    if not data or 'code' not in data or 'analysis_result' not in data:
        return jsonify({"error": "Code and analysis result are required"}), 400

    code = data['code']
    analysis_result = data['analysis_result']
    refactored_code = refactoring_code(code, analysis_result)
    return jsonify({"refactored_code": refactored_code})

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    if not data or 'old_code' not in data or 'old_code_analysis' not in data or 'new_code' not in data:
        return jsonify({"error": "Old code, old code analysis, and new code are required"}), 400

    old_code = data['old_code']
    old_code_analysis = data['old_code_analysis']
    new_code = data['new_code']
    test_result = perform_test(old_code, old_code_analysis, new_code)
    return jsonify({"test_result": test_result})

@app.route('/scan-vulnerability', methods=['POST'])
def scan_vulnerability():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"error": "No code provided"}), 400

    code = data['code']
    vulnerability_result = perform_scan_vulnerability(code)
    return jsonify({"vulnerability_result": vulnerability_result})

# @app.route('/generate-documentation', methods=['POST'])
# def generate_documentation(model, language_to_analyze, directory_path):
#     if not model or not language_to_analyze or not directory_path:
#         return jsonify({"error": "Model, language to analyze, and directory path are required"}), 400

#     documentation_result = create_pdf_crew(model, language_to_analyze, directory_path)
#     return jsonify({"documentation_result": documentation_result})

@app.route('/process-all', methods=['POST'])
def process_all(code, model, language_to_analyze, directory_path):
    data = request.get_json()
    if not data or 'code' not in data or 'model' not in data or 'language_to_analyze' not in data or 'directory_path' not in data:
        return jsonify({"error": "Code, model, language to analyze, and directory path are required"}), 400

    # Step 1: Analyze
    analysis_result = analyze_code(code)

    # Step 2: Refactor
    refactored_code = refactoring_code(code, analysis_result)

    # Step 3: Test
    test_result = perform_test(code, analysis_result, refactored_code)

    # Step 4: Scan for vulnerabilities
    vulnerability_result = perform_scan_vulnerability(refactored_code)

    # Step 5: Generate documentation
    # documentation_result = create_pdf_crew(model, language_to_analyze, directory_path)

    return jsonify({
        "analysis_result": analysis_result,
        "refactored_code": refactored_code,
        "test_result": test_result,
        "vulnerability_result": vulnerability_result,
        # "documentation_result": documentation_result
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=port)
