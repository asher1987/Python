# Your task is to write and test a function which takes three arguments 
#(a year, a month, and a day of the month) and returns the corresponding day 
# of the year, or returns None if any of the arguments is invalid.
# Use the previously written and tested functions. Add some test 
# cases to the code. This test is only a beginning

def isLeapYear(year):
	if year % 4 == 0:
		return True
	elif year % 100 != 0:
		return True
	elif year % 400 == 0:
		return True
	else:
		return False

def daysInMonth(year, month):
	# creating a list that contains the number of days in each month
    # lists are indexed at zero. 
	monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	# Check if the year and month are valid
	if month < 1 or month > 12 or year < 1:
		# if it's not valid, it will return None
		return None
	#Accounting for a Leap year using our isLeapYear function
	if isLeapYear(year):
		# if it is a leap year, we will modify our list at index 1 and change the number
        # of days to 29
        # remember, our list is indexed at zero 
		monthLengths[1] = 29
		# if it is not leap year, return the number of days for that specific month
        # because our list is indexed at zero but our months are indexed at 1, we need to 
        # subtract one from each month to access the correct index
        # Ex: March is the 3rd month, but the monthLength for March is index 2 | (3 - 1 = 2)
		return monthLengths[month - 1]
	
def dayOfYear(year, month, day):
    # Check if the months and days are valid.
    # Months are between 1 and 12
    # Days are between 1 and 31
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
		# if they are not valid, return None
        return None

    # Create a new variable and initialize it (set it equal to)
    # call the function daysInMonth with the two arguments, (year, month)
    # Remember the daysInMonth function determines the number of days in a specific
    # month of a given year, including leap years. It returns the number of days 
    # in that specific month.
    # The returned value is stored in the days_in_month variable 
    days_in_month = daysInMonth(year, month)
	
	# Checks that the provided day is not greater than the number of days 
    # for that specified month (days_in_month)
    # if the condition is not met, it will return None
    # example: If the test code says April has 31 days, it will return None. 
    # April only has 30 days
    if day > days_in_month:
	    return None
	
    # Calculate the day of the year
    #Create a new variable and set it equal to day.
    #day_of_year is used to keep track of the cumulative day count as we iterate through the months. 
    # ex: if your arguments are: year 2023, month = 2 and day = 15, the function initializes day_of_year to 15.
    day_of_year = day

    # Iterate through months leading up to the given month. It will iterate through all the months before the target month
    # inside the loop, i takes on the values from 1(January) up to month - 1. Remember that's how we get the right index
    for i in range(1, month):
        # Get the number of days in each month.
        #We are adding the days of the previous months to the day_of_year variable to keep track of the cumulative day count
        days_in_previous_month = daysInMonth(year, i)

        # Check if the month is valid (daysInMonth didn't return None)
        if days_in_previous_month is None:
            return None

        # Add the number of days in the previous month to the day_of_year
        day_of_year += days_in_previous_month

    return day_of_year



    
# Test cases
print(dayOfYear(2023, 2, 15))  # Valid input
print(dayOfYear(2022, 4, 31))  # Invalid day, returns None
print(dayOfYear(0, 6, 10))     # Invalid year, returns None
print(dayOfYear(2024, 13, 20))  # Invalid month, returns None
