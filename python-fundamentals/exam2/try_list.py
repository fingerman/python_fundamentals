collection = [7, 2, 2, 4, 5, 6, 9] # renaming list variable

row_increased = [x if x % 2 != 0 else x+2 for x in collection]
print(row_increased)