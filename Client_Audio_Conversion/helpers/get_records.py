#!/usr/bin/env python3

import json
import csv
import pandas as pd
from pandas import json_normalize
with open('recordsets.json', 'r') as file:
    df = pd.read_json(file, orient='Value')
    df2 = df.loc[:,1]
    for i in df2:
        #print(i)
        for j in i:
            if hasattr(object, 'Value'):
                print(j['Value'])