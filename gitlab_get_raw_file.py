import requests

gitlab_url = 'https://gitlab.com'
project_id = 'your_project_id'
file_path = 'path/to/your/file.txt'
branch_name = 'master'
access_token = 'your_access_token'

api_url = f'{gitlab_url}/api/v4/projects/{project_id}/repository/files/{file_path}/raw?ref={branch_name}'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    file_content = response.content.decode('utf-8')
    print(file_content)
else:
    print(f'Failed to get file from GitLab API. Status code: {response.status_code}')
