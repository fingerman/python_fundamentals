def n_vocals(string):
    count = 0
    voc = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    for letter in string:
        for vocal in voc:
            if letter == vocal:
                count += 1

    print(count)


n_vocals('fddadasdaoooo')
