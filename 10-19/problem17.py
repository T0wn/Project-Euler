
def int_to_text(nr):
    f = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    s = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if nr < 20:
        return f[nr]
    if nr < 100:
        return s[int(str(nr)[0:1]) - 2] + int_to_text(int(str(nr)[1:2]))
    if nr < 1000:
        if nr % 100 == 0:
            return int_to_text(int(str(nr)[0:1])) + 'hundred'
        return int_to_text(int(str(nr)[0:1])) + 'hundredand' + int_to_text(int(str(nr)[1:]))
    return 'onethousand'

summary = 0
for i in range(1, 1001):
    summary += len(int_to_text(i))

print(summary)