def upper_part(height):
    triangle = ''
    for r in range(1, height):
        for c in range(1, r + 1):
            triangle += str(c) + " "
        triangle += '\n'
    return triangle


def lower_part(height):
    triangle = ''
    for r in range(height, 0, -1):
        for c in range(1, r + 1):
            triangle += f'{c} '
        triangle += '\n'
    return triangle


def draw_triangle(height):
    return upper_part(height) + lower_part(height)


n = int(input())
print(draw_triangle(n))

