def is_palindrome(inp):
    inverse = inp[::-1]
    if inp == inverse:
        return True
    else:
        return False