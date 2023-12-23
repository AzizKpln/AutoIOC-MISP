import requests
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runSSLbl(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    req=requests.get("https://sslbl.abuse.ch/blacklist/sslipblacklist.txt").text
    iocs=req.split("\n")
    for ioc in iocs:
        upload_attr(ioc)
    req1=requests.get("https://sslbl.abuse.ch/blacklist/sslblacklist.csv").text
    lines = req1.split('\n')
    hash_values = [line.split(',')[1] for line in lines if line and not line.startswith("#")]
    for hash_value in hash_values:
        upload_attr(hash_value)
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runSSLbl(MISPAPI,MISPURL,MISPEVENTID)