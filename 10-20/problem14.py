
def evenNumber(number):
    return number / 2

def oddNumber(number):
    return (3 * number) + 1

def nextNumber(number):
    if (number % 2 == 0):
        return evenNumber(number)
    else return oddNumber(number)
