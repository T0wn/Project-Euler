

def isFactor(tall, factor):
    if ( tall % factor == 0 ):
        return True
    return False


def isPrime(tall):
    prime = True

    if ( tall % 2 == 0 ):
        return False
    
    for i in range(3, tall, 2):
        if ( tall % i == 0 ):
            prime = False
            break
        
    return prime

highestNr = 0
n = 600851475143
i = 3
while ( i * i < n ):
    if isFactor(n, i):
        if isPrime(i):
            if i > highestNr:
                highestNr = i
    i+=1

print (highestNr)

wait = input("PRESS ENTER TO CLOSE")
exit()
