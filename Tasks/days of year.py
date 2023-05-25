def year_days(year):
    if year == 0 or year % 4 == 0:
        return str(year) + " " + 'has 366 days'
    else:
        return str(year) + " " + 'has 365 days'


print(year_days(3))

print(-300/4)
