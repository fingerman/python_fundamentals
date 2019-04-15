import os #important
from pathlib import Path
# Path() = os.path.join("../files/more_files/")

print(__file__)                     # path and file name

print(os.path.dirname(__file__))    # path

print(os.listdir("."))              # content in current dir

print(os.path.isdir("names"))       # check if dir exists


target_folder = os.path.join(os.path.dirname(__file__), "names")    # join contents of target folder
print(os.listdir(target_folder))      # important


f = os.path.join(os.path.dirname(__file__), "names", "1.txt")   # important

# with open(f, "r")as target_file:
#      for line in target_file:
#          print(line)

