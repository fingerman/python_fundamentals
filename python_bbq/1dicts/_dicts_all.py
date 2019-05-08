d = {'Pierre': 42, 'Anne': 33, 'Mandrigon': 24, 'Samuel': 27, 'Wolfgang': 29}
print(d.items(), "\n")

print('-----  get value by key ------')
print(d["Pierre"])

print('-----  dictionary.get(keyname, value) - get value by key ------')
print(d.get("Anne"))

print("-----  get value by index")
print(list(d.values())[0])

print("-----  get key by index")
print(list(d.keys())[0])


print("---------  Print Keys ----------------")
for x in d.keys():
    print(x)


print("--------------- Print values------------")
for x in d:
  print(d[x])
# alternative:
for x in d.values():
    print(x)



print("--------Print keys AND/OR values")
for k, v in d.items():
    print(k, v)

print("----------alternative")
for k in d:
    print(k, d[k])

print("----- keys() - returns a list containing the dictionary's keys ")
c = d.keys()
print(type(c))
print(c)
print("----- values() - returns a list containing the dictionary's values ")
b = d.values()
print(type(b))
print(b)



print('----  Update/change certain KEY of a dictionary but keep the value')
d_new = d.copy()
d_new['Pencho'] = d_new['Anne']
del d_new['Anne']
print(d_new.items())
print()

print('---- popitem() removes the last inserted key-value pair -----')
d_new.popitem()
print(d_new)

print(" ----------- dict['KEY'] = dict.pop('KEY') - alternative: ")
d_new['Bamse'] = d_new.pop('Mandrigon')    # d.pop(KEY) - remove element with KEY and return it !
print(d_new.items(), "\n")


print('-----------  Add KEY VALUE pair:')
d['Last'] = 49
print(d.items(), "\n")

print('----Change all VALUES to 0 ---  fromkeys() returns a dict with the specified keys and values.')
d1 = d
d1 = d1.fromkeys(d1, 0)
print(d1.items(), "\n")

print(" ---- setdefault(KEY, VALUE)  returns the value of the item with the specified key. "
      "If the key does not exist, insert the key, with the specified value, see example below")

print(d_new.setdefault('Bamse'))
d_new.setdefault('Set Default', 99)
print(d_new)
















