from flask import request, jsonify
from app import app
from app.services.docs_service import generate_pdf_documentation



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







@app.route('/create-pdf-crew', methods=['POST'])
def create_pdf_crew_controller():

    data = request.json

    print(data)

    model = data['model']
    language_to_analyze = data['language_to_analyze']
    directory_path = data['directory_path']

    print(f"Directory Path : {directory_path}")
    print(f"Language to analyze : {language_to_analyze}")
    print(f"Model : {model}")

    if not model or not language_to_analyze or not directory_path:
        return jsonify({
            "status": "error",
            "message": "Model, language_to_analyze, and directory_path are required fields."
        }), 400
    
    try:
        result = generate_pdf_documentation(
            model=model,
            language_to_analyze=language_to_analyze,
            directory_path=directory_path
        )
        return jsonify({
            "status": "success",
            "message": "PDF crew created and task started successfully.",
            "result": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/hello', methods=['GET'])
def say_hello_controller():
    print("Hello, Welcome on our application !")
    return jsonify({
        "status": "success",
        "message": "Say Hello complete!"
    }), 200
