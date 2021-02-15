import requests
import os
import json
from requests_authlib import 0Auth1

class RequestUtility(object):

    def __init__(self):

    self.env = os.environ.get('ENV', 'uat')
    self.base_url = UAT[self.env]
    self.auth = 0Auth1("Basic bXJkMjp6K01RYWNeP1RyTSZFKH52RzkyVV95")

    def post(self, endpoint, payload=None, headers=None):

        url = self.base_url + endpoint
        import json
        rs_api = request.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)

        import pdb; pdb.set_trace()

def get(self):
pass