import requests

class SonarQubeTool:
    def __init__(self, sonar_url, sonar_token):
        self.sonar_url = sonar_url
        self.sonar_token = sonar_token

    def analyze_code(self, project_key, source_code):
        headers = {'Authorization': f'Bearer {self.sonar_token}'}
        response = requests.post(
            f'{self.sonar_url}/api/projects/analyze',
            headers=headers,
            data={'project': project_key, 'source': source_code}
        )
        return response.json() if response.status_code == 200 else None
