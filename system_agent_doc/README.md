Per suddividere le categorie di input nel controller, possiamo creare una logica che rilevi e gestisca i diversi tipi di input (file singolo, testo, directory in formato path o zip). Qui di seguito è un esempio di come possiamo organizzare il codice per gestire queste diverse categorie in modo chiaro ed efficiente.

### Suddivisione delle Categorie di Input

1. **File Singolo:**
   - Può essere un file `.java` o `.py`.
   - Utilizzare `request.files` per gestire il caricamento del file.

2. **Testo:**
   - Può essere fornito direttamente nel corpo della richiesta JSON.

3. **Directory:**
   - Può essere fornita come path (stringa) nel JSON.
   - Può essere fornita come file `.zip`.

### Esempio di Codice

Ecco come possiamo strutturare il controller per gestire queste categorie:

```python
from flask import Flask, request, jsonify, send_file
import os
import zipfile
import tempfile
import requests

app = Flask(__name__)

# Configurazione dell'API AI
AI_API_URL = 'https://api.ai-documentation.com/generate'
AI_API_KEY = 'your_api_key_here'

def extract_files_from_directory(directory):
    file_contents = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                file_contents[file_path] = f.read()
    return file_contents

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

@app.route('/generateDocumentation', methods=['POST'])
def generate_documentation():
    refactored_code = None

    if 'file' in request.files:
        file = request.files['file']
        file_extension = os.path.splitext(file.filename)[1].lower()
        if file_extension in ['.java', '.py']:
            refactored_code = file.read().decode('utf-8')
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

    elif request.json:
        if 'codeSnippet' in request.json:
            refactored_code = request.json['codeSnippet']
        elif 'directoryPath' in request.json:
            directory_path = request.json['directoryPath']
            if os.path.exists(directory_path) and os.path.isdir(directory_path):
                refactored_code = extract_files_from_directory(directory_path)
            else:
                return jsonify({'error': 'Invalid directory path'}), 400

    elif 'directory' in request.files:
        directory = request.files['directory']
        refactored_code = extract_files_from_zip(directory)
    
    if not refactored_code:
        return jsonify({'error': 'No valid input provided'}), 400

    refactoring_report = request.json.get('refactoringReport', '')
    original_code = request.json.get('originalCode', None)
    config_params = request.json.get('configParams', {})

    # Prepara i dati per l'API AI
    ai_payload = {
        'refactored_code': refactored_code,
        'refactoring_report': refactoring_report,
        'original_code': original_code,
        'config_params': config_params
    }

    try:
        # Chiamata all'API AI per generare la documentazione
        headers = {'Authorization': f'Bearer {AI_API_KEY}', 'Content-Type': 'application/json'}
        response = requests.post(AI_API_URL, json=ai_payload, headers=headers)
        response.raise_for_status()

        # Ottieni la documentazione generata
        documentation = response.json().get('documentation')
        return jsonify({'documentation': documentation})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Spiegazione delle Modifiche

1. **Gestione del File Singolo:**
   - Verifica se il file caricato è un `.java` o `.py`.
   - Legge il contenuto del file.

2. **Gestione del Testo:**
   - Verifica se il corpo della richiesta JSON contiene `codeSnippet`.

3. **Gestione della Directory Path:**
   - Verifica se il corpo della richiesta JSON contiene `directoryPath`.
   - Controlla se il percorso della directory esiste e se è una directory valida.
   - Estrae il contenuto dei file nella directory.

4. **Gestione della Directory Zip:**
   - Verifica se è stato caricato un file zip.
   - Estrae il contenuto dei file dallo zip.

5. **Controlli di Validità:**
   - Se nessuno dei parametri è presente o valido, restituisce un errore.

6. **Prepara i Dati per l'API AI:**
   - Crea un payload JSON con i dati estratti.

7. **Chiamata all'API AI:**
   - Invia i dati nel payload e include l'header di autenticazione.
   - Verifica che la richiesta sia stata eseguita con successo (`raise_for_status`).

8. **Gestione della Risposta:**
   - Ottiene la documentazione generata dalla risposta dell'API AI.
   - Restituisce la documentazione in formato JSON.

### Testare l'API

Puoi testare l'API utilizzando strumenti come `curl`, `Postman` o un form HTML per caricare i file, le directory o il testo.

#### Esempio di Chiamata con `curl`:

**Per un File Singolo:**
```sh
curl -X POST http://localhost:5000/generateDocumentation \
    -F "file=@path_to_your_file.java" \
    -H "Content-Type: multipart/form-data"
```

**Per una Directory Path:**
```sh
curl -X POST http://localhost:5000/generateDocumentation \
    -H "Content-Type: application/json" \
    -d '{
          "directoryPath": "/path/to/your/directory",
          "refactoringReport": "..."
        }'
```

**Per una Directory Zip:**
```sh
curl -X POST http://localhost:5000/generateDocumentation \
    -F "directory=@path_to_your_directory.zip" \
    -H "Content-Type: multipart/form-data"
```

**Per una Porzione di Codice:**
```sh
curl -X POST http://localhost:5000/generateDocumentation \
    -H "Content-Type: application/json" \
    -d '{
          "codeSnippet": "def example_function():\n    pass",
          "refactoringReport": "..."
        }'
```

