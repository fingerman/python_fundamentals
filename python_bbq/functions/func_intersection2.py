vowels = set('aeiouAEIOU')
word = input('Please provide a word to count the vowels: ')
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel, 'was found', word.count(vowel), ' time(s).' )
print(found)


#################

def search4vowels(phrase:str ) ->set:
    vowels = set('aeiouAEIOU')
    return vowels.intersection(set(phrase))


print(search4vowels("fdjslafhudsyipuuuaaaaoo"))

###################


def search4letters(phrase:str, letters:str) ->set:
    """Return letters found in string"""
    return set(letters).intersection(set(phrase))

print("Search4Letters:", search4letters("Hello Worlds", "rl"))