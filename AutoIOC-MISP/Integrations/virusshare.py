import requests
import shutil
import os
import re
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runVirusShare(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    f=requests.get("https://virusshare.com/hashes")
    res=re.findall("hashfiles/VirusShare_\d+",f.text)
    fileName=res[-1].split("/")[1]
    malware_md5=list()
    url1=f"https://virusshare.com/hashfiles/{fileName}.md5"
    local_filename = url1.split('/')[-1]
    with requests.get(url1, stream=True) as r:
        with open("Integrations/"+local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    with open("Integrations/"+local_filename, 'r') as md5_file:
        lines = md5_file.readlines()
    for line in lines:
        if 'http://VirusShare.com' in line or 'Twitter: @VXShare' in line or "################################" in line or "# Malware sample MD5 list for  #" in line or "# VirusShare_00484.zip         #" in line:
            malware_md5.append(line)
    with open("Integrations/"+local_filename, 'w') as md5_file:
        for i in malware_md5:
            md5_file.write(i)
    for line in lines:
        if line not in malware_md5:
            upload_attr(line)
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runVirusShare(MISPAPI,MISPURL,MISPEVENTID)








