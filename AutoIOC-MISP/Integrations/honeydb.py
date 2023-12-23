
import requests
import json
from datetime import datetime
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *

current_date = datetime.now().strftime("%Y-%m-%d")

def runHoneyDB(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    url = 'https://honeydb.io/api/bad-hosts'
    headers = {
        'Accept': 'application/json',
        'X-HoneyDb-ApiId':'93a1d7d4f552a782cf120958f99f86abad8397985161dd78892b3348a467aa91',
        'X-HoneyDb-ApiKey': '022d5de38750eb4bfea60f6dbd49de839e08bfc12aeae3b0e1de2de935ff2b59'
    }
    response = requests.request(method='GET', url=url, headers=headers)
    decodedResponse = json.loads(response.text)
    for i in decodedResponse:
        if str(i["last_seen"])==str(current_date):
            upload_attr(str(i["remote_host"]))
        
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runHoneyDB(MISPAPI,MISPURL,MISPEVENTID)