'''

Problem 1. Date estimation
Input / Constraints
Today is your exam. It’s 26th of August 2018. you will be given a single date in format year-month-day. You should estimate if the date has passed regarding to the date mention above (2018-08-26), if it is not or if it is today. If it is not you should print how many days are left till that date. Note that the current day stills count!
Date Format:
yyyy-mm-dd
Output
The output should be printed on the console.
If the date has passed you should print the following output:
•	"Passed"
If the day is today:
"Today date"
If the date is future:
•	"{number of days} days"



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


