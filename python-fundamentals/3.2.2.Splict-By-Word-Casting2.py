'''
02. Split by Word Casing
Read a text, split it into words and distribute them into 3 lists.
	Lower-case words like “programming”, “at” and “databases” – consist of lowercase letters only.
	Upper-case words like “PHP”, “JS” and “SQL” – consist of uppercase letters only.
	Mixed-case words like “C#”, “SoftUni” and “Java” – all others.
Use the following separators between the words: , ; : . ! ( ) " ' \ / [ ] space
Print the 3 lists as shown in the example below.
Examples
Input	Output
Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.	Lower-case: programming, at, databases, etc
Mixed-case: Learn, SoftUni, Java, 5, Web, C#
Upper-case: PHP, JS, HTML, CSS, SQL, AJAX
Hints
•	Split the input text using the above described separators.
•	Process the obtained list of words one by one.
•	Create 3 lists of words: lowercase words, mixed-case words and uppercase words.
•	Check each word and append it to one of the above 3 lists:
o	Count the lowercase letters and uppercase letters.
o	If all letters are lowercase, append the word to the lowercase list.
o	If all letters are uppercase, append the word to the uppercase list.
o	Otherwise the word is considered mixed-case  append it to the mixed-case list.
•	Print the obtained 3 lists as shown in the example above.


Input
Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.

Output
Lower-case: programming, at, databases, etc
Mixed-case: Learn, SoftUni, Java, 5, Web, C#
Upper-case: PHP, JS, HTML, CSS, SQL, AJAX




'''



input_string = input()
list_separators = [33, 34, 39, 40, 41, 44, 46, 47, 58, 59, 91, 92, 93]
case_lists = [['Lower-case: '], ['Mixed-case: '], ['Upper-case: ']]

for separator in list_separators:
    input_string = input_string.replace(chr(separator), ' ')

words_list = input_string.split()

for word in words_list:
    have_mixed_char = False
    for character in word:
        if ord(character) in range(65):
            have_mixed_char = True
            break
    if word.islower() and not have_mixed_char:
        case_lists[0].append(word)
    elif word.isupper() and not have_mixed_char:
        case_lists[2].append(word)
    else:
        case_lists[1].append(word)

for case_list in case_lists:
    print(case_list[0] + ', '.join(case_list[1:]))