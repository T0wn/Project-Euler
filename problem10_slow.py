

primtall = [2]

summen = 2
x = 3
while ( x < 2000000 ):
    
    for i in primtall:
        isPrim = True
        if ( x % i == 0):
            isPrim = False
            break

    if (isPrime(x):
        primtall.append(x)
        summen += x

    if ( x % 1001 == 0 ):
        print ( "working. checked ", x, " out of 2 000 000" )
        
    x+=2

print(summen)

wait = input("PRESS ENTER TO CLOSE.")
exit()

