import requests
import json

url = "http://localhost:5000/analyze"
headers = {"Content-Type": "application/json"}
data = {"code": "def example():\n    print(\"Hello, World!\")"}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
