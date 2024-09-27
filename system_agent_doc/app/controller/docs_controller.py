import jwt
from flask import request, jsonify

from app import app
from app.services.directory_service import handle_directory_path, handle_directory_zip
from app.services.file_service import handle_file, handle_text

"""

"""
@app.route('/generate_documentation', methods=['GET'])
def generate_documentation_controller():

    print("I'm Here!")
    refactored_code = None

    #refactoring_report = request.json.get('refactoringReport', '')

    #original_code = request.json.get('originalCode', None)

    #config_params = request.json.get('configParams', {})

    if 'file' in request.files:
        print("1 - File uploaded")
        file = request.files['file']
        #refactored_code = handle_file(file)
        return jsonify({'message': 'The file was uploaded'}), 200

    elif request.json:
        print("2 - ")
        if 'codeSnippet' in request.json:
            return jsonify({'success : The code snippet was  uploaded'}), 200
            #refactored_code = handle_text(request.json['codeSnippet'])
        elif 'directoryPath' in request.json:
            directory_path = request.json['directoryPath']
            return jsonify({'message' : 'The directory path was  uploaded'}), 200
            #refactored_code = handle_directory_path(directory_path)
    elif 'directory' in request.files:
        print("3 - ")
        directory = request.files['directory']
        print("Ho caricato lo zip !")
        return jsonify({'success ': 'The directory .zip was  uploaded'}), 200
        #refactored_code = handle_directory_zip(directory)
    return jsonify({'error' : 'The file was not uploaded'}), 500
