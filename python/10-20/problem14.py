
import time
import os

def evenNumber(number):
    return int(number / 2)

def oddNumber(number):
    return (3 * number) + 1

def nextNumber(number):
    if (number % 2 == 0):
        return evenNumber(number)
    else:
        return oddNumber(number)

print("Working...")
start = time.time()


highestRekkeLen = []
for i in range(1, 1000001):
    print(i)
    rekke = [i]
    if (i in highestRekkeLen):
        print("test")
        continue
    while(rekke[len(rekke) - 1] != 1):
        rekke.append(nextNumber(rekke[len(rekke) - 1]))
    if(len(rekke) > len(highestRekkeLen)):
        highestRekkeLen = rekke


os.system("cls")

print(highestLoopCount)

stop = time.time()
print("Cumputing time: " + str(stop-start) + " seconds")

print("")
wait = input("PRESS ENTER TO CLOSE")
exit()
