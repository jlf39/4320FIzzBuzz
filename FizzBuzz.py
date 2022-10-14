def Count():
    x=1
    while x<101:
        printforb(x)
        x=x+1

def printforb(x):
    if x%3 == 0 and x%5 == 0: print("FizzBuzz")
    elif x%3 == 0: print("Fizz")
    elif x%5 == 0: print("Buzz")
    else: print(x)

Count()