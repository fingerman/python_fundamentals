from collections import defaultdict

d = {'Pierre': 42, 'Anne': 33, 'Mandrigon': 24, 'Samuel': 27, 'Wolfgang': 29}
print(d.items(), "\n")

print('Update/change certain KEY of a dictionary')
d_new = d
d_new['Pencho'] = d_new['Anne']
del d_new['Anne']
print(d_new.items())
# alternative:
d_new['Bamse'] = d_new.pop('Pierre')    # d.pop(KEY) - remove element with KEY and return it !
print(d_new.items(), "\n")

print('Add KEY VALUE pair:')
d['Last'] = 49
print(d.items(), "\n")

print('Change all VALUES to 0')
d1 = d
d1 = d1.fromkeys(d1, 0)
print(d1.items(), "\n")

# Change all KEYS to 0. By default DICT cannot have duplicate keys





for row in d.items()



























