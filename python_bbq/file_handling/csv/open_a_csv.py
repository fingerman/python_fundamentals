import csv
'''
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''


# # a - append
# with open('datei.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=';')
#     writer.writerow(['Roberto', '859455321', 'Rome', 'Italy'])

# create the file if it does not exist
with open('dateia.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Datei A', '859455321', 'Rome', 'Italy'])

f = open('datei_a')