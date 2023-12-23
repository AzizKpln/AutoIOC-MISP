import requests
import os
import re
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runVXVault(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    req=requests.get("http://vxvault.net/URL_List.php").text
    iocs=req.split("\n")
    for ioc in iocs:
        upload_attr(ioc)

if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runVXVault(MISPAPI,MISPURL,MISPEVENTID)