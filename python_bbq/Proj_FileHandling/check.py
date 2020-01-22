import os


target_folder = os.path.join(os.path.dirname(__file__), "names")

n = 0
for file in os.listdir(target_folder):
    files = open(os.path.join(target_folder, file))
    for line in files:
        data = line.strip().split(' ')
        if data[0] == "Max":
            n += 1
    files.close()
print(n)
