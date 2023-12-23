from pymisp import PyMISP, MISPEvent
import requests
import re
import sys

def misp_connect(mispapi,mispurl,mispeventid):
    global event
    global misp
    global event_id
    misp_url = mispurl
    misp_key = mispapi
    misp_verifycert = False
    event_id = mispeventid
    session = requests.Session()
    session.verify = misp_verifycert
    PyMISP.global_session = session
    misp = PyMISP(misp_url, misp_key, ssl=False)
    event = misp.get_event(event_id)
    print(misp_url,misp_key,mispeventid)
def upload_attr(attribute):
    def identify_string(input_string):
        ip = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        md5_pattern = re.compile(r'^[a-fA-F0-9]{32}$')
        sha256_pattern = re.compile(r'^[a-fA-F0-9]{64}$')  
        domain = re.compile(r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b')
        url = re.compile(r'\b(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]')

        if ip.match(input_string):
            return "IP Address"
        elif md5_pattern.match(input_string):
            return "Hash_MD5"
        elif sha256_pattern.match(input_string):
            return "Hash_SHA256"
        elif domain.match(input_string):
            return "Domain"
        elif url.match(input_string):
            return "URL"
        else:
            return "Unknown"
    if event is None:
        print(f'Error: Event with ID {event_id} not found.')
        exit()
    try:
        if identify_string(attribute) == "IP Address":
            attribute = {
                'type': 'ip-dst',
                'value': attribute
            }
        elif identify_string(attribute) == "Domain":
            attribute = {
                'type': 'domain',
                'value': attribute
            }
        
        elif identify_string(attribute) == "URL":
            attribute = {
                'type': 'url',
                'value': attribute
            }
        elif identify_string(attribute) == "Hash_SHA256":
            attribute = {
                'type': 'sha256',
                'value': attribute
            }
        elif identify_string(attribute) == "Hash_MD5":
            attribute = {
                'type': 'md5',
                'value': attribute
            }
        try:
            misp.add_attribute(event_id, attribute)
            print(f'Successfully added IOC: {attribute}.')
        except Exception as e:
            print(f'Error adding attribute: {e}')
    except IndexError:
        print("Usage: python3 main.py <ioc_list.txt>")
