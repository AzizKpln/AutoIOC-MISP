import csv
import requests
from io import StringIO
import os
import re
try:
    from Integrations.mispIntegration import *
except:
    from mispIntegration import *
def runURLHaus(mispapi,mispurl,mispeventid):
    misp_connect(mispapi,mispurl,mispeventid)
    url = 'https://urlhaus.abuse.ch/downloads/csv_recent/'
    response = requests.get(url)
    if response.status_code == 200:
        csv_data = response.text
        csv_file = StringIO(csv_data)
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            if len(row) >= 9:
                upload_attr(row[2])
            else:
                print("Error: Row does not have the expected number of columns")

    else:
        print(f"Error fetching data. Status code: {response.status_code}")
if __name__=="__main__":
    if os.path.exists("MISP/Info"):
        with open("MISP/Info","r") as f:
            a=f.readlines()
            MISPAPI=a[0].split("MISPAPI:")[1].strip()
            MISPURL=a[1].split("MISPURL:")[1].strip()
            MISPEVENTID=a[2].split("MISPEVENTID:")[1].strip()
            runURLHaus(MISPAPI,MISPURL,MISPEVENTID)
