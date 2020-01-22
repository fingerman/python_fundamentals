from os import strerror

try:
    stream = open("C:\\Project\\python\\python_bbq\\data_file_handling\\daei.txt", "rt")
    print(stream.read())
except IOError as exc:
    print("open failed:", strerror(exc.errno))
