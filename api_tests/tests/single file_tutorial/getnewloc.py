import json
import requests

base_url = "https://uat-api2.mrdcourier.com/api/api/clients/3/locations/${id}"

headers = {"Content-Type" : "application/json"}

username = "mrd2"
password = "z+MQac^?TrM&E(~vG92U_y"

rs_api = requests.post(url=base_url, data=json.dumps(payload), headers=headers, auth=(username, password))

print(rs_api.text)

