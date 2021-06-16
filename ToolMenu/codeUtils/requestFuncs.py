import os

import requests


def upload(fileName):
    files = {'upload_file': open(fileName, 'rb')}
    values = {'DB': 'hs', 'OUT': 'pcap'}
    r = requests.post(os.getenv("Request_url"), files=files, data=values)
    return r;
