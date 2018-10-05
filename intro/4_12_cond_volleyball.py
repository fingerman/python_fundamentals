import math

yearType = input()
holidays = int(input())
weekendsHome = int(input())

if yearType == 'leap':
    weekendsSofia = 48 - weekendsHome
    saturdayGames = weekendsSofia * (3/4)
    gamesHome = weekendsHome
    gamesAll = saturdayGames + gamesHome
    gamesHolidays = holidays * (2/3)
    gamesTotal = (gamesAll + gamesHolidays)
    gamesTotalLeap = ((gamesTotal * 15)/100) + gamesTotal
    print(math.floor(gamesTotalLeap))
elif yearType == 'normal':
    weekendsSofia = 48 - weekendsHome
    saturdayGames = weekendsSofia * (3/4)
    gamesHome = weekendsHome
    gamesAll = saturdayGames + gamesHome
    gamesHolidays = holidays * (2/3)
    gamesTotal = (gamesAll + gamesHolidays)
    print(math.floor(gamesTotal))

