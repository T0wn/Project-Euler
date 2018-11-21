
import math

sumOfSquares = 0
summen = 0

for i in range(1, 101):
    summen += i
    sumOfSquares += math.pow(i, 2)

summen = math.pow(summen, 2)

print(summen - sumOfSquares)

wait = input("PRESS ENTER TO CLOSE")
exit()
