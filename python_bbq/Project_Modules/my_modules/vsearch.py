#################


def search4vowels(phrase: str) ->set:
    """Return any vowels in phrase"""
    vowels = set('aeiouAEIOU')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str) ->set:
    """Return letters found in string"""
    return set(letters).intersection(set(phrase))

