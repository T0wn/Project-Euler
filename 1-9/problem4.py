
#eks, reversererTall(123) = "321"
def reverserTall(tall):
    return (str(tall)[::-1])

#palindrome er tall som har speila halvdeler, eks: 100001, 1001, 2332 
def sjekkOmPalindrome(tall):
    halvLengde = int(len(str(tall)) / 2)
    x = str(tall)[halvLengde:]
    y = str(tall)[:halvLengde]
    return( x == reverserTall(y) )

highestNr = 0
x = 999
while ( x > 800 ):
    y = 999
    while ( y > 800 ):
        if (sjekkOmPalindrome(x*y)):
            if ( (x*y) > highestNr ):
                highestNr = x*y
                print(x*y)
        y-=1
    x-=1
    

wait = input("PRESS ENTER TO CONTINUE.")
exit()
