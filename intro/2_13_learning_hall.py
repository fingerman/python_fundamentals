

h = float(input())*100
w = float(input())*100
used = (3*(70*120)) + 100*h
space_available = h*w - used
print("space available " + str(space_available))
places = space_available / (70*120)
print(str(places))
