
import time
import os

startTime = time.time()

def xThPrime(x):
    primes = [2]
    y = 3
    while ( len(primes) <= x ):
        prime = True
        for i in range(0, len(primes)):
            if y % primes[i] == 0:
                prime = False
                break
        if prime:
            primes.append(y)
        y += 1
    return primes[x-1]

print ("Working...")

svar = xThPrime(10001)
stopTime = time.time()

os.system('cls')
print (svar)
print ("Runtime: ", round((stopTime - startTime), 2), " seconds")

print("")
wait = input("PRESS ENTER TO CLOSE")
exit()
