import pandas as pd
import os
import json
import glob

# reading all Big json files that need to be split - refactor of deprecated code
path_to_read_json = 'my_path'
all_files = glob.glob(path_to_read_json + 'file-*')
print("All files: ", all_files)

path_to_dump_jsons = 'Sarah_Jsons/'

for big_json in all_files:
    # fetching name of big json
    big_json_name = big_json.split('/')[-1]
    print(big_json_name)
    with open(os.path.join(big_json), 'r', encoding='utf-8') as big_json:
        
        ll = [json.loads(line.strip()) for line in big_json.readlines()]

        # total length size of the json file - each line is 1 call
        print("Total length of the json: ", len(ll))

        # define your size of split - 20 calls in current case
        size_of_the_split = 20
        total_splits = len(ll) // size_of_the_split

        #Total number of splits
        print("Total number of splits: ", total_splits + 1)

        for i in range(total_splits + 1):
            
            json.dump(ll[i * size_of_the_split:(i + 1) * size_of_the_split], open(
                path_to_dump_jsons + big_json_name + "_split_" + str(i+1) + ".json", 'w',
                encoding='utf8'), ensure_ascii=False, indent=True)

print("Files saved at: ", path_to_dump_jsons)