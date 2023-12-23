import requests
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runPhishHunt(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    req=requests.get("https://phishunt.io/feed.txt").text
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
            runPhishHunt(MISPAPI,MISPURL,MISPEVENTID)