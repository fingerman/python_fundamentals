total_days = int(input())
n_users_day = int(input())
money_single_user = float(input())
money_all_users = money_single_user * n_users_day
words = []

for i in range(n_users_day):
    words += [int(input())]

for i in words:
    if i > 5:
        n_users_day = n_users_day - 1

counter = 0
for x in range(1, n_users_day+1):
    if x % 3 == 0:
        counter += 2
n_users_day = n_users_day + counter


for i in words:
    if i == 1:
        n_users_day = n_users_day + 1

total = total_days * n_users_day * money_single_user


print(words)
print("Total words earned for " + str(total_days) + " days: " + "{0:.2f}".format(total))

'''

10          
6             
6           
1           
1
1
1
1
1
##3
10          
3            
6           
1           
1
1
##2
10          
2            
6           
1           
1


'''