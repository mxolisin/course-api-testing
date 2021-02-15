import json
import requests

base_url = "https://uat-api2.mrdcourier.com/api/clients/3/locations"

payload = {
    "businessName": "Bussiness K",
    "street": "22 Castle Close",
    "suburb": "Brackenfell",
    "city": "Cape Town",
    "province": "Western Cape",
    "postalCode": "7560",
    "countryCode": "ZA",
    "addressType": "BUSINESS",
    "buildingType": "House",
    "lat": -33.8983550,
    "lng": 18.6903071
}

headers = {"Content-Type" : "application/json"}

username = "mrd2"
password = "z+MQac^?TrM&E(~vG92U_y"

rs_api = requests.post(url=base_url, data=json.dumps(payload), headers=headers, auth=(username, password))

print(rs_api.text)