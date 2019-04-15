found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
found['e'] += 1
found['e'] += 1
print(found)

# {'a': 0, 'e': 2, 'i': 0, 'o': 0, 'u': 0}

for k in found:
    print(k, " found ", found[k], " times")