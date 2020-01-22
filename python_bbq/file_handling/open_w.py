'''
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''

# open("file_name", 'a')

f = open('datei_write.txt', 'w')
f.write("Name;Phone;City;Country3")
f.close()

f = open('datei_write.txt', 'r')
print(f.read())
f.close()








