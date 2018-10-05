num = int(input())


to20 = {0:'', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
over20 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


if 1 <= num <= 19:
    print(to20[num])
elif 20 <= num <= 99:
    tens, below_ten = divmod(num, 10)
    print(over20[tens - 2] + ' ' + to20[below_ten])
elif num == 100:
    print("one hundred")
elif num == 0:
    print("zero")
elif num < 0:
    print("invalid number")
elif num > 100:
    print("invalid number")

