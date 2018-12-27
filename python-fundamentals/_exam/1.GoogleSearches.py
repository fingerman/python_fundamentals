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

'''

10          
4             
6           
6           
1
3
6

        3 users
10 x ([6] + [6] + [(2*1)*3*6)])
10 x 48

10 x 18 x 3
'''