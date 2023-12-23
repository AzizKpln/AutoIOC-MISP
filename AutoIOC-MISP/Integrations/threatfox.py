import requests
from io import BytesIO
from zipfile import ZipFile
import os
import re
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *

def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file '{file_path}': {e}")
def download_and_extract(url, destination_folder):
    response = requests.get(url)
    if response.status_code == 200:
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(destination_folder)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
def read_content():
    with open("Integrations/full_domains.json","r",encoding="utf-8") as dom:
        domains =dom.readlines()
        for domain in domains:
            if "ioc_value" in domain:
                domain_=domain.strip().split(":")[1]
                domain_=domain_.split('"')
                domain_=domain_[1]
                upload_attr(domain_)
              
    with open("Integrations/full_sha256.json","r") as f:
        ioc_list=f.readlines()
        for j in ioc_list:
            if "ioc_value" in j:
                ioc=j.strip().split(":")[1]
                ioc=ioc.split('"')
                ioc=ioc[1]
                upload_attr(ioc)
    with open("Integrations/full_ip-port.json", "r") as f:
        ioc_list = f.readlines()
        for line in ioc_list:
            if "ioc_value" in line:
                ioc = line.strip().split(":")[1]
                ioc = ioc.split('"')
                ip_address = ioc[1]
                upload_attr(ip_address)

def runThreatFox(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    zip_url = ["https://threatfox.abuse.ch/export/json/sha256/full/","https://threatfox.abuse.ch/export/json/ip-port/full/","https://threatfox.abuse.ch/export/json/domains/full/"]
    destination_folder = "Integrations/"
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for url in zip_url:
        download_and_extract(url, destination_folder)
    read_content()
    for r in list(["Integrations/full_sha256.json","Integrations/full_ip-port.json","Integrations/full_domains.json"]):
        delete_file(str(r))
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runThreatFox(MISPAPI,MISPURL,MISPEVENTID)
    
