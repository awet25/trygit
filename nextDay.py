
def numberOfDays(month,year):
    daysInMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(year%4==0 and year %100 !=0) or (year % 400==0):
        daysInMonth[1]=29
    return daysInMonth[month-1]



def nextDay(year,month,day):
    nbDays = numberOfDays(month,year)
    if day < nbDays:
        day += 1
    elif day == nbDays:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    res = '['+str(year)+'-'+str(month)+'-'+str(day)+']'
    print(res)

nextDay(2024,12,31)