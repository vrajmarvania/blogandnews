import requests
import json
url = 'http://127.0.0.1:8000/B/submit'
data = {
    'blog_title': 'Mohinee',
    'blog_content': 'aaaaa',
}
json_data=json.dumps(data)
r=requests.post(url=url,data=json_data)

data=r.json()
print(data)


