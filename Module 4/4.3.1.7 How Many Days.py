# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days 

#for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense

## code from 4.2.1.6 that tests for Leap Year
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


	

## Test code provided 
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


