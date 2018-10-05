def triangle_area():
    a = float(input())
    h = float(input())
    area = (a*h)/2
    print('{0:.12g}'.format(area))

# f'{area:.12g}'   - alternative printing, no tuple indexing


triangle_area()

