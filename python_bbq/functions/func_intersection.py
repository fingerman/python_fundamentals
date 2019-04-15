def volews_search(inp):
    vowels = set('aeiou')
    all_vowels = vowels.intersection(list(inp))
    return all_vowels


print(volews_search('dasiodasdadsadsayyyseeefdsafda'))

