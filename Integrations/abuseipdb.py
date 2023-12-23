
import requests
import json
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *

def runAbuseIP(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    url = 'https://api.abuseipdb.com/api/v2/blacklist'
    querystring = {
        'confidenceMinimum':'85'
    }
    headers = {
        'Accept': 'application/json',
        'Key': '438fad635ef39a0a143ffe7ab3f77ecba1f1cae0ef974c6ce16bd5ae6199b104fb780d282f2b1e9e'
    }
    print("[+] Geting IOC List From AbuseipDB. Please wait!")
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)
    def extract_ip_addresses(data):
        try:
            json_data = json.loads(data)
            ip_addresses = [entry["ipAddress"] for entry in json_data.get("data", [])]
            return ip_addresses
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"
    ip_addresses = extract_ip_addresses(json.dumps(decodedResponse, sort_keys=True, indent=4))
    for i in ip_addresses:
        upload_attr(i)
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runAbuseIP(MISPAPI,MISPURL,MISPEVENTID)