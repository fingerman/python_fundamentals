angaben = [['NA', 12, 5, 78], [2, 13, 5, 7], [2, 'NA', 5, 78], [2, 14, 5, 39], [3, 13, 'NA', 7]]


def new_func(lst):
    if 'NA' not in lst:
        return True


neu_ang = list(filter(new_func(angaben), angaben))

print(neu_ang)