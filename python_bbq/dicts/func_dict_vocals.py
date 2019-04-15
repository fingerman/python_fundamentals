def dict_vocals(string):
    string = string.lower()
    count_vocals = 0
    count_cons = 0
    voc_dict = {}
    cons_dict = {}
    voc = ['a', 'e', 'i', 'o', 'u']
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ß']
    for letter in string:
        for vocal in voc:
            if letter == vocal:
                if vocal not in voc_dict:
                    count_vocals = 0
                count_vocals += 1
                voc_dict[vocal] = count_vocals

        for consonant in cons:
            if letter == consonant:
                if consonant not in cons_dict:
                    count_cons = 0
                count_cons += 1
                cons_dict[consonant] = count_cons

    print("Vowels: ", voc_dict)
    print("Consonants: ", cons_dict)


dict_vocals('Hallo Welt')
