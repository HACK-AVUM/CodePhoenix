from flask import request, jsonify
from app import app
from app.services.scanning_vulnerability_service import perform_scan_vulnerability


@app.route('/scanning-vuln', methods=['POST'])
def scanning_vulnerability_code(code):

    vuln = perform_scan_vulnerability(code)

    return 0
