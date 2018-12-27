n_homes = int(input())
n_init_presents = int(input())
list_presents = []
for i in range(n_homes):
    list_presents.append(int(input()))
n_all_hpresents = sum(list_presents)


n_more_presents = n_init_presents /

if n_init_presents <= n_all_hpresents:
    print(n_init_presents - n_all_hpresents)




'''
Problem 1 – Hogswatch
Here is the problem, the Hogfather can travel to all the homes in one night it’s a wonder right! But somehow he just can’t handle math. He forgot the number of presents he has to give, all that he can remember is the number of homes. You need to help him and save Hogswatch!!!
You are given the number of homes N the Hogfather has to visit, on the first line.
And then the total number of presents he took when leaving the workshop on the second line.
In each home Hogfather visits he counts the number of socks above the fireplace and gives you that number. If he runs out of presents he has to go back to the workshop for more. 
The number of presents he has to get is equal to the integer value of initial presents divided (integer division) by homes visited including the current one. Multiplied by the number of remaining homes, plus the number of presents he needs in addition for the current home or in other words:
({initialPresents} / {visitedHomes}) * {remainingHomes} + {additionalPresents}
There are two possible outputs:
•	If the initial number of presents is enough you print the remaining presents on a single line
-	On a single line the number of presents left - {presentsNumber}
•	If the Hogfather run out of presents at some point print two lines
-	On the first line print – total number of times he went back - {timesBack}
-	On the second line print – total number of presents he took in addition - {additionalPresentsTaken}
Input / Constraints
•	On the first line N  homes to visit – integer in range [1 - 100]
•	On the second line – initial number of presents – integer in range [1 – 10000]
•	On the next N lines the number of children per house – integer in range[1-100]
•	Input will always be valid and in the range specified you don’t need to check it
Output
•	On of the two possible outputs specified above
Examples
Input	Output	Comment
5
20
2
1
3
9
5	

0	

The Hogfather needs to visit 5 homes
He went out with 20 presents
In the first house he left 2 presents, then in the second he left 1 present. After that he left 3 presents, then 9 presents, and in the last house 5 presents. There were enough presents so out of 20 he gave 20 and we print 0 as the ramaining number of presents.

4
20
12
10
3
9	

1
22	

The Hogfather needs to visit 4 homes
He went out with 20 presents
In the first house he left 12 presents, then in the second, he have to leave 10 presents, but he has only 8 left. So he goes back, the number of presents he takes this time is equal to 20 (initial presents) devided by homes visited so far (including current home) multiplied by 2 (homes remaining) that is equal to 20 then we add 2 presents he needs to leave in the current home. So he goes back 1 time and brings 22 presents. He moves to the next homes, but he doesn’t go back anymore.
5
10
4
5
3
4
5	

2
11	

The Hogfather needs to visit 5 homes
He went out with 10 presents
At the first home he left 4 presents. At the second home he left 5 presents. At the third home he has only 1 present remaining so he needs to go back for more. He takes (10 / 3) * 2 + 2 = 8 presents, then leaves 2 in the current home. He moves to the fourth home, here he leaves 4 presents. At the fifth home he needs to leave 5 presents, but he has only 2, so he goes back second time. He takes (10 / 5) * 0 + 3 = 3 presents. So in total he went back 2 times and got totally 11 presents 8 the first time and 3 the seocond.


'''