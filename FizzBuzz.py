def Count():
    x=1
    while x<101:
        printforb(x)
        x=x+1

def printforb(x):
    if x%3 == 0: print("Fizz")
    if x%5 == 0: print("Buzz")
    if x%3 !=0 and x%5 !=0: print(x)

Count()