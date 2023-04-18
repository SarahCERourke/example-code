#!/usr/bin/env python
import json
import os
import json
from pprint import pprint


# json file or files to be validated and reformatted into proper json if needed.

json_file = "*.json"

#jsondir = f"/mnt/efs/{folder}/json"
#file_names =  os.listdir(jsondir)
def return_json(json_file):
    #jsondir = f"{folder}/"
    #file_names = os.listdir(jsondir)
    #for i in file_names:
    with open(json_file, 'r') as opened_file:
        new_format = json.load(opened_file)
    
    pprint(new_format)
    
    #for i in file_names:
    #    with open(f'{folder}/{i}', 'w') as opened_file:
    #        new_format = json.dump(new_format, opened_file)
            
            

return_json(json_file)