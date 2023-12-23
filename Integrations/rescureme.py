import requests
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runRescureMe(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    req=requests.get("https://rescure.me/rescure_blacklist.txt").text
    lines = req.split('\n')
    ip_addresses = [line.strip() for line in lines if line and line[0].isdigit()]
    for ip_address in ip_addresses:
        upload_attr(ip_address)
    req1=requests.get("https://rescure.me/rescure_malware_hashes.txt").text
    lines = req1.split('\n')
    hash_values = [line.strip() for line in lines if line and len(line) == 40]
    for hash_value in hash_values:
        upload_attr(hash_value)

    req1=requests.get("https://rescure.me/rescure_domain_blacklist.txt").text
    lines = req1.split(' # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    lines=lines[2].split("\n")
    for i in lines:
        if i=="":
            pass
        else:
            upload_attr(i.strip())
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runRescureMe(MISPAPI,MISPURL,MISPEVENTID)