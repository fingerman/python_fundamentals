def draw_tree(num):
    for rows in range(0, num):
        print('*' * rows)
    for rows in range(num//2):
        print('*' * (num//3))


draw_tree(20)