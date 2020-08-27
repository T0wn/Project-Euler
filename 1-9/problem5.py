
'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

import time
import math

startTid = time.time()

for i in range(20, 10000000000, 20):
    korrekt = True
    for t in range(2, 20):
        if ( i % t != 0 ):
            korrekt = False
            break
    if (korrekt):
        print (i)
        break

stoppTid = time.time()
print("Runtime: ", (round((stoppTid-startTid), 2)), "seconds")

wait = input("PRESS ENTER TO CLOSE")
exit()
