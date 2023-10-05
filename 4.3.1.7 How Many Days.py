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

def daysInMonth(year, month):
	monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if month < 1 or month > 12 or year < 1:
		return None
	if isLeapYear(year):
		monthLengths[1] = 29
		#lists are indexed at zero
        # months are indexed at 1
        # ex: March is the third month, but it's index is 2
		return monthLengths[month - 1]


	


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


