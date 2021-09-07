import json, os, requests, sys
from collections import defaultdict

if len(sys.argv) < 2:
    print('Error: command')
    sys.exit(0)
k = sys.argv[1]

filename = os.path.join(os.path.dirname(__file__), 'stats')

if os.path.exists(filename):
    with open(filename, 'r') as f:
        j = defaultdict(int, json.load(f))
else:
    j = defaultdict(int)

if k in ['plan', 'apply']:
    j[k] += 1
else:
    sys.exit(0)

text = 'Terraform today: ' + ', '.join([f'{value} {key}' for key, value in j.items()])

MM_URL = os.getenv('MM_URL')
MM_TOKEN = os.getenv('MM_TOKEN')

h = {'Authorization': f'Bearer {MM_TOKEN}'}
d = {'props': {'customStatus': f"{{\"emoji\":\"terraform\",\"text\":\"{text}\",\"duration\":\"\",\"expires_at\":\"0001-01-01T00:00:00Z\"}}"}}
r = requests.put(f'{MM_URL}/api/v4/users/me/patch', headers=h, json=d)
if r.status_code != 200:
    print('Error: bad response')

with open(filename, 'w') as f:
    json.dump(j, f)
