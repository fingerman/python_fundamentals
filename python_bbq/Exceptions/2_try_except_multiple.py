try:
    x = int(input())
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print('Cannot divide by zero – sorry!')
except ValueError:
    print('You have to enter an integer value!')
except:
    print('Something else got wrong')
print('THE END')

'''
This is how it works:

- if the try branch raises the exc1 exception, it will be handled by the except exc1: block;
- similarly, if the try branch raises the exc2 exception, it will be handled by the except exc2: block;
- if the try branch raises any other exception, it will be handle by the unnamed except block.
'''
