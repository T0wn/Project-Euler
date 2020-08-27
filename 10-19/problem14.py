
import time

def evenNumber(number):
    return int(number / 2)

def oddNumber(number):
    return (3 * number) + 1

def nextNumber(number):
    if (number % 2 == 0):
        return evenNumber(number)
    return oddNumber(number)

def roundToOdd(number):
    if (number % 2 == 0):
        return number - 1
    return number


max_number = 1000000


print("Working...")
start = time.time()

highestRekkeLen = []
for i in range(roundToOdd(max_number), int(max_number / 2), -2):
    rekke = [i]
    if (i in highestRekkeLen):
        continue
    while(rekke[-1] != 1):
        rekke.append(nextNumber(rekke[-1]))
    if(len(rekke) > len(highestRekkeLen)):
        highestRekkeLen = rekke



stop = time.time()
print(highestRekkeLen[0])
print("Cumputing time: " + str(stop-start) + " seconds")

