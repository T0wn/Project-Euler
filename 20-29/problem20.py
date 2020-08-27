
def factorial(nr):
    value = 1
    for i in range(nr, 1, -1):
        value *= i
    return value

def split_sum(nr):
    value = 0
    for i in str(nr):
        value += int(i)
    return value

print(split_sum(factorial(100)))