
distance = float(input())
distanceInMeters = distance
arg2 = input()
arg3 = input()


if arg2 == 'mm':
    distanceInMeters = distance / 1000

elif arg2 == 'cm':
    distanceInMeters = distance / 100

elif arg2 == "mi":
    distanceInMeters = distance / 0.000621371192

elif arg2 == "in":
    distanceInMeters = distance / 39.3700787

elif arg2 == "km":
    distanceInMeters = distance / 0.001

elif arg2 == "ft":
    distanceInMeters = distance / 3.2808399

elif arg2 == "yd":
    distanceInMeters = distance / 1.0936133


outDistance = distanceInMeters


if arg3 == 'mm':
    outDistance = distanceInMeters * 1000

elif arg3 == 'cm':
    outDistance = distanceInMeters * 100

elif arg3 == "mi":
    outDistance = distanceInMeters * 0.000621371192

elif arg3 == "in":
    outDistance = distanceInMeters * 39.3700787

elif arg3 == "km":
    outDistance = distanceInMeters * 0.001
elif arg3 == "ft":
    outDistance = distanceInMeters * 3.2808399

elif arg3 == "yd":
    outDistance = distanceInMeters * 1.0936133


print("{0:.8f}".format(outDistance), arg3)

