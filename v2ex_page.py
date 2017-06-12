import json,requests
r = requests.get('https://www.v2ex.com/api/topics/hot.json')
print(r.json())