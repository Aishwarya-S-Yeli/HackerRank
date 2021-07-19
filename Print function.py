# Task
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

# Input format:
# The first line contains an integer n.

# Output format:
# Print the list of integers from 1 throughn as a string, without spaces.

# Code

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end='');
