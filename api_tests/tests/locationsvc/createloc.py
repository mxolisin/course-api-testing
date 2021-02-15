import json
import requests

def test1():
    App_URL="http://log-location-svc.gcp.mrdexpress.uat/api/clients/3/location.json"
    f = open('/Users/mxolisi.ngcobo/mrd_automation/apachejmeter/jmeterScripts/LPT - LOG Planning/TEST PLANS/LPT-3510 | LPT | QA - Add update location endpoint/Location svc.jmx', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_Url, request_json)
    print(response.text)
