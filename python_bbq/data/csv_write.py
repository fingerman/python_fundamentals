import csv

# with open('datei.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=';')
#    # reader.writerow(['Roberto'])
#     for row in reader:
#         print(row)

with open('datei.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=':')
    writer.writerow(['Roberto', '859455321', 'Rome', 'Italy'])

