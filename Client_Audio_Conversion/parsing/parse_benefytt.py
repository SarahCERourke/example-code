import collections
import pandas as pd
import os
import json
import numpy as np
import csv

rootdir = '/mnt/efs/benefytt'
jsondir = os.path.join(rootdir, 'json')
loc = os.path.join(rootdir, '06-13-metadata.csv')

df = pd.read_csv(loc)

df = df[["recording_name", "ANI", "AGENT_FIRST_NAME", "AGENT_LAST_NAME"]]
df = df.rename(columns={"AGENT_FIRST_NAME": "agent_name", "AGENT_LAST_NAME": "agent_id", "ANI": "recording_id"})

# edit recording names to remove spaces and add underscores 
#df['recording_name_clean'] = df['recording_name'].replace(" ", "_")[:-4]
df['recording_name_clean'] = df.apply(lambda row: row['recording_name'].replace(' ', '_')[:-4], axis=1)

# validation
json_flnames = [flname for flname in os.listdir(jsondir)
                if flname[-len('.json'):] == '.json'
            ]
         
json_recording_ids = set([os.path.splitext(os.path.splitext(json_flname)[0])[0]
    for json_flname in json_flnames])

extract_fl_shared_uid = lambda json_flname: os.path.splitext(os.path.splitext(json_flname)[0])[0]
#print(extract_fl_shared_uid)

Row = collections.namedtuple('Row', ('external_id', 'rec_start', 'rec_end', 'speaker_channel', 'type', 'content'))

# use transcript json data and reformat to print as one line in conversation.
make_content = lambda voci_utterance: ' '.join([event['word'] for event in voci_utterance['events']])

make_row_ = lambda voci_utterance, recid: Row(
    external_id=recid,
    #recording_id=recid,
    rec_start=voci_utterance['recvdate'][:-7],
    rec_end=voci_utterance['donedate'][:-7],
    speaker_channel=voci_utterance['metadata']['channel'],
    #agent_id=agent_id,
    #agent_name=agent_name,
    type='Agent' if voci_utterance['metadata']['channel'] == 0 else 'Visitor',
    content=make_content(voci_utterance))


make_rows_ = lambda json_flname, recid: [
    make_row_(voci_utterance, recid)
    for voci_utterance in json.load(open(os.path.join(jsondir, json_flname)))['utterances']]
make_rows = lambda json_flname: make_rows_(json_flname, extract_fl_shared_uid(json_flname))


# assert all([
csvdir = '/mnt/efs/benefytt/csv'
if not os.path.exists(csvdir):
    os.makedirs(csvdir)
    
convs = []
for i, json_flname in enumerate(json_flnames):
    if i % 20 == 0:
        fl_index = i // 20
        if len(convs) > 0:
            df2 = pd.DataFrame.from_records(convs, columns=Row._fields) #.to_csv(open(os.path.join(csvdir,'{}_last.csv'.format(fl_index)), 'w'), header=header_list, index=False)
            df_merged = df.merge(df2, left_on='recording_name_clean', right_on='external_id')
            df_merged = df_merged.drop(columns=["recording_name", "recording_name_clean", "recording_id"])
            df_merged['recording_id'] = df_merged.apply(lambda row: row['external_id'].split('_')[0], axis=1)
            df_merged = df_merged[["external_id", "recording_id", "rec_start", "rec_end", "agent_id", "agent_name", "speaker_channel", "type", "content"]]
            df_merged.to_csv(open(os.path.join(csvdir,'{}.csv'.format(fl_index)), 'w'), index=False)
        convs = []
    rows = make_rows(json_flname)
    convs.extend(rows)
    #print(convs)

fl_index = i // 20
df2 = pd.DataFrame.from_records(convs, columns=Row._fields) #.to_csv(open(os.path.join(csvdir,'{}_last.csv'.format(fl_index)), 'w'), header=header_list, index=False)
df.merge(df2, left_on='recording_name_clean', right_on='external_id').to_csv(open(os.path.join(csvdir,'{}_last.csv'.format(fl_index)), 'w'), index=False)


#["external_id", "recording_id", "rec_start", "rec_end", "speaker_channel", "type", "content"]