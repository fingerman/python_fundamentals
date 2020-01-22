'''

The try statement in Python can have an optional finally clause.
This clause is executed no matter what, and is generally used to release external resources.
'''

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()        # the file is closed even if an exception occurs.