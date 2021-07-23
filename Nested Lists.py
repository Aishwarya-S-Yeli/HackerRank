# Task
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of 
# any student(s) having the second lowest grade.

# Input format:
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Output format:
# Print the name(s) of any student(s) having the second lowest grade in. 
# If there are multiple students, order their names alphabetically and print each one on a new line.

# Code
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desired_students = []
    for stu in students:
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))
