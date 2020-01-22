class CriticalError(Exception):
    def __init__(self, message='ERROR MESSAGE A'):
        Exception.__init__(self, message)

raise CriticalError

#raise CriticalError("Error Message B")
