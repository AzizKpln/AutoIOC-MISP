import requests
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runCinsScore(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    req=requests.get("https://cinsscore.com/list/ci-badguys.txt").text
    ipAddr=req.split("\n")
    for i in ipAddr:
        upload_attr(i)
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runCinsScore(MISPAPI,MISPURL,MISPEVENTID)