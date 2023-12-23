import requests
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runOpenPhish(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    req=requests.get("https://openphish.com/feed.txt").text
    req_=req.split("\n")
    for i in req_:
        upload_attr(i)
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runOpenPhish(MISPAPI,MISPURL,MISPEVENTID)