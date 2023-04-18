import pandas as pd
import os
import json
import csv
import glob

# older code used for parsing processed json files, post transcription by voci's vblaze api. used for one client.

# reading all jsons
path_to_read_json = 'Sarah_Jsons/'
all_files = glob.glob(path_to_read_json + '*.json')

# Printing all the jsons
# print(all_files)

path_to_transcribed_csvs = 'Sarah_transcribed_csvs/'
for index, json_file in enumerate(all_files):
    
    # fetching name of json
    json_name = json_file.split('/')[-1].split('.')[0]
    
    # opening a csv based on index to create 1 csv per json
    with open(path_to_transcribed_csvs + json_name + "_" + f'{index}' + '.csv', 'w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=["external_id", "recording_id", "rec_start", "rec_end",
                                                        "speaker_channel", "agent_id", "agent_name", "message_type", "content"])

        csv_writer.writeheader()
            # opening 1 json file at a time
        with open(json_file) as json_file:
            full_json = json.load(json_file)
            
            # going over 1 transcript at a time
            for full_transcript in full_json:

                # going over each row per transcript
                for f_row in full_transcript:
                    # fetching static keys that need to be filled on all lines
                    message_type = f_row.get('messageType')

                    if message_type == 'callStart':
                        f_recording_id = f_row.get('csid','')

                    if message_type == 'conversationStart':
                        f_agent_name = f_row.get('callcenterID', '')
                        f_agent_id = f_row.get('agentID', '')
                        break

                for f_row in full_transcript: # voce_utterance is same as f_row above

                    external_id = f_row.get('crn', '')
                    recording_id = f_recording_id
                    rec_start = full_transcript[0].get('timestamp',''),  # first element is call start object
                    rec_end = full_transcript[-1].get('timestamp', '')
                    speaker_channel = f_row.get('speaker', 'system')  # voci_utterance['metadata']['speakerTurn'],
                    agent_id = f_agent_id
                    agent_name = f_agent_name
                    message_type = f_row.get('messageType', '')
                    content = ''
                    # getting content
                    content_list = []
                    if message_type == 'speakerTurn':
                        for item in f_row['nbest']:
                            content_list.append(item['transcription'])
                        content = ' '.join(content_list)   


                    row = {"external_id": external_id, 
                            "recording_id": recording_id, 
                            "rec_start": rec_start[0], 
                            "rec_end": rec_end, 
                            "speaker_channel": speaker_channel, 
                            "agent_id": agent_id, 
                            "agent_name": agent_name, 
                            "message_type": message_type, 
                            "content": content}

                    csv_writer.writerow(row)



