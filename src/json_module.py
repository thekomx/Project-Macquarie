import requests
import json

class getJSON:
    status_code = ''
    reason = ''
    json = ''

    def __init__(self, url):
        req = requests.get(url)

        self.status_code = req.status_code
        self.reason = req.reason

        if req.status_code == 200:
            json_data = json.loads(req.text)
        else:
            json_data = req.reason

        self.json = json_data