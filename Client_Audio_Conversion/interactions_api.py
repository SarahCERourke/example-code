#!/usr/bin/env python3

import requests
import pandas as pd
import os
from pathlib import Path
import csv
import time

customer = "ipg"
json_dir = f"/mnt/efs/{customer}/json/"

file_names = os.listdir(json_dir)

file_list = []
for i in file_names:
    file_name = ''.join(i.split(".json"))
    time.sleep(7)

#file_list.extend([file_name] * 10)
#print(file_list)

    Headers = {"Content-Type": "application/json", "RateLimit-Limit": "", "Authorization": ""}

    url = ""


    data = {
        "data": [
            #file_list
            f'{file_name}'
        ]
    }
    
    response = requests.post(url, json=data, headers=Headers)
    response.raise_for_status()
    data = response.json()
    for i in data:
        i["id"]
        json_file_name = i["id"]
        #print(json_file_name)
        with open(f"/mnt/efs/ipg/call_metadata_json/{json_file_name}.json", "w") as f:
            f.write(response.text)