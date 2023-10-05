# create a function with one argument, (year)
# and returns True if the year is a leap year
# or false otherwise 

def isLeapYear(year):
    if (year % 4 == 0 # checks if divisible by 4
        and year % 100 !=0 #if it is divisible by 100 it is not a leap year
        ) or (year % 400 == 0): #it is a leap year if it divisible by 400
        return True
    else:
        return False
# function that takes two arguments, (year, month)
def daysInMonth(year, month):
    # create a list with the days for each month, index 1
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # checks if the year given is a leap year using
    # the 'isLeapYear' function, and if the month == 2 (Feb)
    if isLeapYear(year) and month == 2:
        # if both conditions are met, it returns 29 
        # 29 is the number of days in Feb during a leap year
        return 29
    # check sif the month is with the 1-12 range
    elif 1 <= month <= 12:
        # if it is, it returns the number of days for that month using the [month-1]
        # the -1 is used because lists are indexed at zero
        return monthDays[month - 1]
    # if the month is not valid (not between 1 and 12,) return none
    else:
        return None

#function takes three arguments, (year, month, day)
def dayOfYear(year, month, day):
    #this line makes sure the inputs are valid
    # is the month between 1 and 12 and is the day is between 1 and 31
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        # if none of these conditions are met it returns none
        return None 
    
    # this initializes a new variable, total_days and sets it equal to day
    # day is is the paramter that is passed to the function and represents the 
    # the specific day of the month we're trying to caclulate
    total_days = day
    
    #creates a loop that iterates from 1 to month - 1
    # this loop is used to add the number of days in each month 
    for m in range(1, month):
        #this adds the number of days in each month 
        total_days += daysInMonth(year, m)
    # this returns the total_days which represents the day of the year 
    return total_days

print(dayOfYear(2000, 12, 31))