def remove_negative(number):
    return number[1:] if number[0] == '-' else number


def even_odd_product(number):
    evens = 0
    odds = 0
    for c in range(0, len(number)):
        current = int(number[c])
        if current % 2 == 0:
            evens += current
        elif current % 2 != 0:
            odds += current
    return evens * odds


def evens_by_odds(number):
    return even_odd_product(remove_negative(number))


print(evens_by_odds(input())