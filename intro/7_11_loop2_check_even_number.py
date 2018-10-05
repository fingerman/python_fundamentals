while 1:
    try:
        print('Enter even number: ', end='')
        number = int(input())
        if number % 2 == 1:
            print('The number is not even.')
        else:
            print('Even number entered: {0}'.format(number))
            break
    except:
        print('Invalid number!')