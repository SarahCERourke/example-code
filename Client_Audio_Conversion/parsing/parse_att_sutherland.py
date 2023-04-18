import json
import xml.etree.ElementTree as ET
import pathlib as Path
import os
import pandas as pd
import numpy as np

# Declare directory of the att-sutherland metadata files in xml format and
# then iterate through the directory to call each file name for parsing
xmldir = "/mnt/efs/att-sutherland/call_metadata"

xml_flnames = [
    filename for filename in os.listdir(xmldir)
    if filename[-len('.xml'):] == '.xml'
]

for f, filename in enumerate(xml_flnames):
    f = os.path.join(xmldir, filename)

    #print(f) # to check that each filename is getting output to the terminal
    tree = ET.parse(f)
    root = tree.getroot()
    # the block of data in the xml is and object "recording"
    # the attributes are childern of the object and a pia
    for i in root.findall('recording'):
        att_uid = i.find('ATTUID').text
        bpo_name = i.find('BPOName').text
        agent_id = i.find('AgentID').text
        agent_name = i.find('AgentName').text
        ani = i.find('ANI').text
        start_date = i.find('StartDate').text
        end_date = i.find('EndDate').text
        time_zone = i.find('TimeZone').text
        duration = i.find('Duration').text
        call_id = i.find('CallID').text
        file_name = i.find('Filename').text
        direction = i.find('Direction').text
        extension = i.find('Extension').text
        dnis = i.find('dnis').text
        number_of_hold = i.find('NumberOfHold').text
        total_hold_time = i.find('TotalHoldTime').text
        ucid = i.find('UCID').text
        split_id = i.find('SplitID').text
        split_desc = i.find('SplitDesc').text
    # format data into DataFrame, call rstrip() to remove each trailing white space which were present on most strings
    data = [
        f'{att_uid.rstrip()}', f'{bpo_name.rstrip()}', f'{agent_id.strip()}',
        f'{agent_name.rstrip()}', f'{ani.rstrip()}', f'{start_date.rstrip()}',
        f'{end_date.rstrip()}', f'{time_zone.rstrip()}',
        f'{duration.rstrip()}', f'{call_id.rstrip()}', f'{file_name.rstrip()}',
        f'{direction.rstrip()}', f'{extension.rstrip()}', f'{dnis.rstrip()}',
        f'{number_of_hold.rstrip()}', f'{total_hold_time.rstrip()}',
        f'{ucid.rstrip()}', f'{split_id}', f'{split_desc}'
    ]
    df = pd.DataFrame([data])
    print(df) # output to terminal for validation
    # writes DataFrame to csv using the append mode - add a header after by rewriting the file.
    df.to_csv('test-4.csv', mode='a', index=False, header=False)
    
    # read original csv file with pandas
    file = pd.read_csv('test-4.csv')
    # Describe headers in list
    headerList = ['ATTUID', 'BPOName', 'AgentID', 'AgentName', 'ANI', 'StartDate', 'EndDate', 'TimeZone', 'Duration', 'CallID', 'Filename', 'Direction', 'Extension', 'dnis', 'NumberOfHold', 'TotalHoldTime', 'UCID', 'SplitID', 'SplitDesc']
    # Write original file plust headerlistto new file
    file.to_csv("att-sutherland-call-metadata.csv", header=headerList, index=False)

