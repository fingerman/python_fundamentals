'''02.
Split by Word Casing
Read a text, split it into words and distribute them into 3 lists.
	Lower-case words like “programming”, “at” and “databases” – consist of lowercase letters only.
	Upper-case words like “PHP”, “JS” and “SQL” – consist of uppercase letters only.
	Mixed-case words like “C#”, “SoftUni” and “Java” – all others.
Use the following separators between the words: , ; : . ! ( ) " ' \ / [ ] space
Print the 3 lists as shown in the example below.
Examples
Input:
Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.

Output:
Lower-case: programming, at, databases, etc
Mixed-case: Learn, SoftUni, Java, 5, Web, C#
Upper-case: PHP, JS, HTML, CSS, SQL, AJAX
'''

data = input()
list_separators = [',', ';', ':', '.', '!', '(', ')', '\"', '\'',  '\\',  '/', '[', ']']

for separator in list_separators:
    data = data.replace(separator, ' ')

list_lower = []
list_upper = []
list_mixed = []


def is_upper(word):
    for letter in word:
        if not (letter>='A' and letter<'Z'):
            return False
    return True


for word in data.split():
    if word.islower():
        list_lower.append(word)
    elif is_upper(word):
        list_upper.append(word)
    else:
        list_mixed.append(word)

print(f"Lower-case: {', '.join(list_lower)}")
print(f"Mixed-case: {', '.join(list_mixed)}")
print(f"Upper-case: {', '.join(list_upper)}")



