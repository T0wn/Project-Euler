
def isTripple(tall):
    if (tall % 3 == 0):
        return True
    return False

def isFive(tall):
    if (tall % 5 == 0):
        return True
    return False

summen = 0

for i in range(3, 1000):
    if (isFive(i) | isTripple(i)):
        summen += i

print(summen)

wait = input("PRESS ENTER TO CLOSE")
exit()
