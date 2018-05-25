
import math

# CTN initialise
currentTriangleNumber = 1
currentTriangleNumberValue = 1

def increseCTN(increse):
    global currentTriangleNumber
    global currentTriangleNumberValue
    for i in range(0, increse):
        currentTriangleNumber += 1
        currentTriangleNumberValue += currentTriangleNumber

def getNumberOfDivisors(number):
    divisors = 0
    for i in range(1, int(math.ceil(math.sqrt(number)))+1):
        if(number % i == 0):
            divisors += 1
    return ((divisors * 2) - 1)


while (True):
    if (getNumberOfDivisors(currentTriangleNumberValue) > 500):
        print(currentTriangleNumberValue)
        break
    increseCTN(1)


print("")
wait = input("PRESS ENTER TO CLOSE")
exit()
