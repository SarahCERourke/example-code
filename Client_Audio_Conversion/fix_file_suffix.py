#!/usr/bin/env python3
import json
import os

folder = "folder_name"


#jsondir = f"/mnt/efs/{folder}/json"
#file_names =  os.listdir(jsondir)
def my_function(folder):
    jsondir = f"{folder}/json/"
    file_names = os.listdir(jsondir)
    for i in file_names:
        print(i)
        old_name = i
        new_name = '_transcript.json'.join(i.split(".wav.json"))
        os.rename(jsondir + old_name, jsondir + new_name)

my_function(folder)