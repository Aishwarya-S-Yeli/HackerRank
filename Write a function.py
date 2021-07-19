# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# Input format
# Read year, the year to test.

# Output format
# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

# Code

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

year = int(raw_input())
print is_leap(year)
