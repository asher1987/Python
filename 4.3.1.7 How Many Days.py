# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days 

#for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense

def isLeapYear(year):
	if year % 4 == 0:
		return True
	elif year % 100 != 0:
		return True
	elif year % 400 == 0:
		return True
	else:
		return False

def days_in_month(year, month):
    # List of days in each month
    monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the year and month are valid
    if month < 1 or month > 12 or year < 1:
        return None

    # Adjust February for leap years.
    # Checks to see if the year is a leap year
    if isLeapYear(year):
		# if it is a leap year, we modify the list, monthLengths index 1 to 29. 
        # Lists are indexed at 0. So the value that would correspond to February would be at index 1
        monthLengths[1] = 29
    #this is going to return the number of days in the month. 
    # The months are numbered 1-12 but our list is indexed at 0. So we need to subtract one to make sure we are accessing the correct index
    # Ex:  March is the 3rd month but it has an index of 2 | ( 3 - 1 = 2)
    return monthLengths[month - 1]



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")