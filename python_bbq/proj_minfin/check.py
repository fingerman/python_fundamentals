import os

#target_folder = os.path.join(os.path.dirname(__file__), "names")

tar_folder = 'F:\minfinleak2\BulgariaNRA_RF\MINFIN_BREACH'
target_folder = os.path.join(tar_folder, 'AZ')



n = 0
for file in os.listdir(target_folder):
    files = open(os.path.join(target_folder, file), encoding="utf8")
    for line in files:
        data = line.strip().split(',')
        n += 1
    files.close()
print(n)
