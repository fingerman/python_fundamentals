def PrintExcTree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end='')
    if nest > 0:
        print("   +---", end='')
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        PrintExcTree(subclass, nest + 1)


PrintExcTree(BaseException)
