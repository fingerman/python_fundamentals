'''The continue statement continues with the next iteration of the loop.'''
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


''' break - terminates the loop containing it '''
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")
