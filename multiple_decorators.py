def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    print( "Hello Sally")

@changecase
def otherfun():
    print("I am speed")

myfunction()

otherfun()