import requests
from base64 import b64encode

TEMP_FILE = 'tmp.tmp'

url = 'https://duckduckgo.com/html/'
payload = {'q': 'python'}
r = requests.get(url, params=payload)


url = '===='
client = requests.session()
client.get(url)


data = {
    "email": "====",
    "password": "====",
    'ci_csrf_token': client.cookies['ci_csrf_token']
}

client.post(url, data=data)
recieved_data = client.get(url)

with open(TEMP_FILE, 'w') as file:
    file.write(recieved_data.text)

