import zipfile
import tempfile
import os

####################################### PATH  ###############################
"""

"""
def extract_files_from_directory(directory):
    file_contents = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                file_contents[file_path] = f.read()
    return file_contents

"""

"""
def handle_directory_path(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        return extract_files_from_directory(directory_path)
    else:
        raise ValueError('Invalid directory path')

#######################################  ZIP  ###############################

"""
"""
def extract_files_from_zip(zip_file):
    file_contents = {}
    with tempfile.TemporaryDirectory() as tempdir:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(tempdir)
        for root, _, files in os.walk(tempdir):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    file_contents[file_path] = f.read()
    return file_contents
"""

"""
def handle_directory_zip(directory):
    return extract_files_from_zip(directory)
