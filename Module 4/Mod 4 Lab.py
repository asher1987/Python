def isLeapYear(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False
    
def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeapYear(year) and month == 2:
        return 29
    elif 1 <= month <= 12:
        return monthDays[month - 1]
    else:
        return None

    
def dayOfYear(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return None 
    
    total_days = day
    for m in range(1, month):
        total_days += daysInMonth(year, m)
        
    return total_days

print(dayOfYear(2000, 12, 31))