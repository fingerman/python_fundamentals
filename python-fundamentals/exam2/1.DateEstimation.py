'''
INPUT
2018-08-20

Output
Passed
--------------------------
Input
2021-08-26

1097 days left
--------------------------
Input -  today
2018-08-26

Today date
'''


import datetime


list_nums = [int(item) for item in input().split('-')]
date_input = datetime.date(list_nums[0], list_nums[1], list_nums[2])
date_today = datetime.datetime.now().date()



if date_today == date_input:
    print("Today date")
if date_input < date_today:
    print("Passed")
if date_input > date_today:
    days_left = date_input - date_today
    days_left = days_left +  datetime.timedelta(days=1)
    print(f'{days_left.days} days left')


