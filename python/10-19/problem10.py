
# funnet på https://stackoverflow.com/questions/17524685/project-euler-10-python
def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print (sumPrimes(2000000))

wait = input("PRESS ENTER TO CLOSE.")
exit()

