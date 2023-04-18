import collections
import pandas as pd
import os
import json
import numpy as np


jsondir = '/mnt/efs/anthem_archive/elevance-4-15-22/audio/markashby_376_595_json'

json_flnames = [flname for flname in os.listdir(jsondir)
                if flname[-len('.json'):] == '.json'
            ]
json_recording_ids = set([os.path.splitext(os.path.splitext(json_flname)[0])[0]
                      for json_flname in json_flnames])


extract_fl_shared_uid = lambda json_flname: os.path.splitext(os.path.splitext(json_flname)[0])[0]



Row = collections.namedtuple('Row', ('external_id', 'recording_id', 'rec_start', 'rec_end', 'speaker_channel', 'agent_id', 'agent_name', 'type', 'content'))

make_content = lambda voci_utterance: ' '.join([event['word'] for event in voci_utterance['events']])

make_row_ = lambda voci_utterance,recid: Row(
    external_id=recid,
    recording_id=recid,
    rec_start=voci_utterance['recvdate'],
    rec_end=voci_utterance['donedate'],
    speaker_channel=voci_utterance['metadata']['channel'],
    agent_id=recid,
    agent_name=recid,
    type='Agent' if voci_utterance['metadata']['channel'] == 0 else 'Visitor',
    content=make_content(voci_utterance))


make_rows_ = lambda json_flname, recid: [
    make_row_(voci_utterance, recid)
    for voci_utterance in json.load(open(os.path.join(jsondir, json_flname)))['utterances']]
make_rows = lambda json_flname: make_rows_(json_flname, extract_fl_shared_uid(json_flname))

# check_in_DF_ = lambda edf, extracted_suid: 

# create csv directory if needed
csvdir = '/mnt/efs/anthem_archive/elevance-4-15-22/audio/markashby_376_595_csv'
if not os.path.exists(csvdir):
    os.makedirs(csvdir)

convs = []
for i, json_flname in enumerate(json_flnames):
    if i % 20 == 0:
        fl_index = i // 20
        if len(convs) > 0:
            pd.DataFrame.from_records(convs, columns=Row._fields).to_csv(open(os.path.join(csvdir,'{}.csv'.format(fl_index)), 'w'), index=False)
        convs = []
    rows = make_rows(json_flname)
    convs.extend(rows)

fl_index = i // 20
pd.DataFrame.from_records(convs, columns=Row._fields).to_csv(open(os.path.join(csvdir,'{}_last.csv'.format(fl_index)), 'w'), index=False)

    
