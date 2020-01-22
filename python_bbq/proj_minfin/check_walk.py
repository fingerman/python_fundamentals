import os
import csv


tar_folder = 'F:\minfinleak2\BulgariaNRA_RF\MINFIN_BREACH'
dir_tree = os.walk(tar_folder)


for k, v, list_csv_files in dir_tree:
    for csv_file in list_csv_files:
        files = open(os.path.join(k, csv_file), encoding='utf')
        for line in files:
            data_line = line.strip().split(',')
            if '5809157935' in data_line:
                print(csv_file)
                print("Your name was found in Database:", k.split('\\')[4], ";     Table: ", csv_file)
                print(data_line)
        files.close()

