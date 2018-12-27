'''
Task 1.
Google Seaches
You will be given several lines of input and you must calculate how much money Google makes from user searches. On the first line you will receive total days. On the second line you will receive the number of users (n) that make google searches for a single day. Then, you will receive the money Google makes from a single search of a user. On the next n lines you will get the words that each user has in his search. You have to calculate the total money from the searches for the given days. However there are some additional rules:
•	If the words a user uses are greater than 5, we ignore the search and we do not calculate the money from it
•	If the search contains only one word, the money from the search are doubled
•	Money made by each third user are tripled.
After calculating the total money, print them in the following format:
“Total money earned for {days} days: {totalMoney}”. The money should me formatted to the second decimal point.
message.
Input
•	First line: total days, integer in range [0, 1000]
•	Second line: number of users (n), integer in range [0, 10000]
•	Third line: money per search, floating-point number in range [0, 5000]
•	Next n lines: words in range [0, 10]
Output
•	Print the output in the format described above
Constraints
•	The command will always be valid.
•	The messages will always be one word string.
•	Allowed working time / memory: 100ms / 16MB.
Examples
Input
5
2
5.5
6
1

Output:
Total money earned for 5 days: 55.00
Comments:
We ignore the money from the first user. For the second user we have one word, so we double the money (11). Then we multiply them by 5 days, so we get a total money of 55.00
55 = (5.5 * 2) * 5

Input:
10
3
6
5
4
1

Output:
Total money earned for 10 days: 480.00
'''


total_days = int(input())
n_users_day = int(input())
money_single_search = float(input())

words = []
for i in range(n_users_day):
    words += [int(input())]

# remove if 5 > money_single_user
for i in words:
    if i > 5:
        words.remove(i)
# make double user amount if one word per search and rest = money_single_search
words = [x * 2 * money_single_search if x == 1 else 6 for x in words]
# triple amount of each 3rd user
words = [x*3 if i % 3 == 0 else x for i, x in enumerate(words, 1)]

total = total_days * sum(words)

print("Total words earned for " + str(total_days) + " days: " + "{0:.2f}".format(total))

