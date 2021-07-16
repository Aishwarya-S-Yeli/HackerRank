# Task
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b. 
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.

# Input format: 
# The first line contains the first integer, a.
# The second line contains the second integer, b.

# Output format:
# Print the two lines as described above.

# CODE

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

div1 = a//b
div2 = a/b

print (div1)
print (div2)
