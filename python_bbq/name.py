'''
__name__ is a built-in variable which evaluates to the name of the current module.

Thus it can be used to check whether the current script is being run on its own
or being imported somewhere else by combining it with if statement, as shown below.
'''

print("File1 __name__ = %s" % __name__)

if __name__ == "__main__":
    print("File1 is being run directly")
else:
    print("File1 is being imported")
