'''
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''

# open("file_name", mode='r')  - defualt mode
print("----------  read(n)  -----")     # - return all or N first character. Return empty string at the end
f = open('datei.txt', 'rb') # - the file must exists
print(f.read())
f.close()

print("-------------")

print('-------  readline() ------')# - Read and return complete line from the file.
                                    #  Reads in at most n bytes if specified.
f = open('datei.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline(20))
f.close()

print('-------  readlines() ------') # return a list of all lines from the file.
                                     # Reads in at most n bytes/characters if specified.
                                     # - returns empty list if nothing to read
f = open('datei_append.txt', 'r')
print(f.readlines())
f.close()


print("-----  read with loop from open() --------") # !!! open() - the object is an instance of the iterable class.
f = open('datei.txt', 'r+')
for i in f:
    print(i)
f.close()
