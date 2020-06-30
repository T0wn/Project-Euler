
def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if year % 400 == 0:
            return 28
        if year % 4 == 0:
            return 29
        return 28
    return 31

def getWeekday(year, month):
    currentWeekday = 0
    for y in range(1900, year):
        for m in range(1, 13):
            currentWeekday = (currentWeekday + days_in_month(y, m)) % 7
    for m in range(1, month):
        currentWeekday = (currentWeekday + days_in_month(year, m)) % 7
    return currentWeekday

def sunday_in_start(stop_year):
    startingSundays = 0
    currentWeekday = 0
    for year in range(1900, stop_year + 1):
        for month in range(1, 13):
            currentWeekday = (currentWeekday + days_in_month(year, month)) % 7
            if currentWeekday == 6:
                startingSundays += 1
    return startingSundays


print(sunday_in_start(2000) - sunday_in_start(1901))
print(getWeekday(2020, 8))