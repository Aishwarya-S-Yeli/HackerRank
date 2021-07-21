# Task
# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
# Print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum of i+j+k is not equal to n. 
# Here, 0<=i<=x; 0<=j<=y; 0<=k<=z . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Input format: Four integers x, y, z and n, each on a separate line.

# Output format: Print the list in lexicographic increasing order.

# Code

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    output = [];
    abc = [];
    for x in range(x+1):
        for y in range(y+1):
            for z in range(z+1):
                if x+y+z != n:
                    abc = [x,y,z];
                    output.append(abc);
print(output);
