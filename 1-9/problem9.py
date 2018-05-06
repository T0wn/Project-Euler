
import math

a = 0
while ( a < 500 ):
    b = 0
    while ( b < 500 ):
        c = math.sqrt( math.pow(a, 2) + math.pow(b, 2) )
        if ( a + b + c == 1000 ):
            print (int(a*b*c))
            wait = input("PRESS ENTER TO CLOSE.")
            exit()
        b+=1
    a+=1

