import os


############################ FILE .java , .py ########################

def handle_file(file):
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension in ['.java', '.py']:
        return file.read().decode('utf-8')
    else:
        raise ValueError('Unsupported file type')

############################ TEXT ##############################

def handle_text(code_snippet):
    return code_snippet
