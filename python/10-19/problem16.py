
number = str(pow(2, 1000))

summary = 0
for i in range(len(number)):
    summary = summary + int(number[i])

print(summary)