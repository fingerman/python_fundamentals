from my_modules import search4letters


def vsearch(phrase, letters='aeiouAEIOU'):
    return search4letters(phrase, letters)


print(vsearch("Hello World. What is going on ?", "lc"))
