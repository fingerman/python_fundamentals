'''

each raised exception falls into the first matching branch;
the matching branch doesn’t have to specify the same exception exactly –
it’s enough that the exception is more general (more abstract) than the raised one.

If more abstract Exception is met first, a more specific is not needed.

- the order of the branches matters!
- don’t put more general exceptions before more concrete ones;
- this will make the latter one unreachable and useless;

'''


try:
    y = 1 / 0
except ZeroDivisionError:
    print('Zero division!')
except ArithmeticError:             # Arithmetic Error is superclass
    print('Arithmetic problem!')
print('THE END')

print('-----------')


try:
    y = 1 / 0
except ArithmeticError:
    print('Arithmetic problem!')
except ZeroDivisionError:
    print('Zero division!')
print('THE END')