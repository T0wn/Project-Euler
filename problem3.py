
def isFactor(tall, factor):
    if ( tall % factor == 0 ):
        return True
    return False

def arrayPrimes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False
    return sieve

'''
def isPrime(tall):
    prime = True

    if ( tall % 2 == 0 ):
        return False
    
    for i in range(3, tall, 2):
        if ( tall % i == 0 ):
            prime = False
            break
        
    return prime
'''

primes = arrayPrimes(600851475143)
for i in range(0, 600851475143):
    if (primes[i]):
        print (i)
    

wait = input("PRESS ENTER TO CLOSE")
exit()
