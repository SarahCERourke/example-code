#!/usr/bin/env python
import os
from os.path import exists

audio_list = []
converted_list = []
json_list = []

folder = "folder_name"

def folder_difference(folder):
    audiodir = f'{folder}/audio/'
    converteddir = f'{folder}/converted/'
    jsondir = f'{folder}/json/'
    
    audio_files = os.listdir(audiodir)
    for i in audio_files:
        audio_list.append(''.join(i.split('.wav')))
    print("number of audio files = " f'{len(audio_list)}')
    
    converted_files = os.listdir(converteddir)
    for i in converted_files:
        converted_list.append(''.join(i.split('.wav.wav')))
    print("number of converted files = " f'{len(converted_list)}')
    
    json_files = os.listdir(jsondir)
    for i in json_files:
        json_list.append(''.join(i.split('_transcript.json')))
    print("number of completed json files = " f'{len(json_list)}')
    
    diff_list = []
    for i in audio_list:
        if i not in json_list:
            diff_list.append(i)
   # print(diff_list)
    print(len(diff_list))
    
    new_list = []
    for i in json_list:
        audio_file = f'{i}.wav'
        audio_file_path = audiodir + audio_file
        if os.path.exists(audio_file_path):
            new_list.append(i)
            print("deleting " + audio_file_path)
            os.remove(audio_file_path)
            print("deleted " + f'{len(new_list)}' + " files")                
        print("doesnt exist")
    #for i in json_list:
        #converted_file = f'{i}.wav.wav'
        #converted_file_path = converteddir + converted_file
        #if os.path.exists(converted_file_path):
        #    new_list.append(i)
        #    print("deleting " + converted_file_path)
        #    os.remove(converted_file_path)
        #    print("deleted " + f'{len(new_list)}' + " files.")
        #print("doenst exist")
        
folder_difference(folder)
    