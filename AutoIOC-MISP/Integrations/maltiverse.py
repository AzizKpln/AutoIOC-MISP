
import requests
import os
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runMaltiverse(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIzMTkzNTg5MzcsImlhdCI6MTY4ODYzODkzNywic3ViIjoxNjA5NSwidXNlcm5hbWUiOiJheml6a2FwbGFuMTkwNyIsImFkbWluIjpmYWxzZSwidGVhbV9pZCI6bnVsbCwidGVhbV9uYW1lIjpudWxsLCJ0ZWFtX2xlYWRlciI6ZmFsc2UsInRlYW1fcmVzZWFyY2hlciI6ZmFsc2UsInRlYW1faW5kZXgiOm51bGwsImFwaV9saW1pdCI6MTAwfQ.JLvydZA3dd-fKO0TZQzHlU0ckoBDfpVQGEk_S-AeWWM'
    url = 'https://api.maltiverse.com/collection/WZ0XJHIB8jmkCY9eLpr0/download?filetype=sha256'
    headers = { 'Authorization':'Bearer ' + api_key }
    response = requests.get(url, headers=headers)
    re=response.text
    r=re.split("\n")
    for i in r:
        upload_attr(i)
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runMaltiverse(MISPAPI,MISPURL,MISPEVENTID)