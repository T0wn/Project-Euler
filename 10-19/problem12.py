
import math
import time
import os

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

start = time.time()
print("Working...")

while (True):
    if (getNumberOfDivisors(currentTriangleNumberValue) > 500):
        break
    increseCTN(1)

stop = time.time()
os.system('cls')

print(currentTriangleNumberValue)
print("Cumputing time: " + str(stop-start) + " seconds")

print("")
wait = input("PRESS ENTER TO CLOSE")
exit()
