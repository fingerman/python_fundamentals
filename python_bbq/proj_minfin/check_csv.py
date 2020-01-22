import os
import csv


tar_folder = 'F:\mfleak\databg\ALL_BREACH'
dir_tree = os.walk(tar_folder)

n = 0
for k, v, list_csv_files in dir_tree:
    for csv_file in list_csv_files:
        with open(os.path.join(k, csv_file), encoding='utf') as f:
            reader = csv.reader(f)
            data = [r for r in f]
            for data_line in data:
                if '8503267924' in data_line:
                    n += 1
                    print("Името Ви беше намерено в база данни:", k.split('\\')[4], ";     Таблица: ", csv_file)
                    print("Обозначения:")
                    print(data[0], end='')
                    print("Записани данни:")
                    print(data_line)
print('Общо: ', n, ' резултата')





