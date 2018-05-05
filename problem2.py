

def isEven(number):
    if (number % 2 == 0):
        return True
    else:
        return False

summen = 0
rekke = [1, 2]

while ( rekke[len(rekke)-1] < 4000000 ):
    if isEven( rekke[len(rekke)-1] ):
        summen += ( rekke[len(rekke)-1] )

    rekke.append( rekke[len(rekke)-1] + rekke[len(rekke)-2] )


print (summen)

wait = input("PRESS ENTER TO CLOSE.")
exit()
