'''
Write a program that takes a text and a string of banned words.
 All words included in the ban list should be replaced with asterisks "*",
 equal to the word's length. The entries in the ban list will be separated by a space " ".
The ban list should be entered on the first input line and the text on the second input line.
Example:

    Input

Linux Windows
It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client

Output

It is not *****, it is GNU/*****. ***** is merely the kernel,
while GNU adds the functionality. Therefore we owe it to them
by calling the OS GNU/*****! Sincerely, a ******* client


words = list(input().split(' '))
text = input()

filtered = text
for word in words:
    filtered = filtered.replace(word, '*' * len(word))
print(filtered)
'''

banned_words = input().split()
text = input()


for word in banned_words:
    text = text.replace(word, '*'*len(word))
print(text)
