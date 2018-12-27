
"""
Given the names and grades for each student in a Physics class of N
students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints:
2<=N<=5
There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""

if __name__ == '__main__':

    python_students = []
    
    for _ in range(int(input("Enter value of n :"))):
        name = input("Your name:")
        score = float(input("Your score"))

        python_students.append([score,name])

python_students.sort()

print(python_students)

temp = min(python_students)

capture = []
for i in range(len(python_students)):
    if python_students[i] == temp:
        capture.append(python_students[i])
        capture.append(python_students[i+1])
        
capture2 = []
for i in capture:
    for j in i:
        capture2.append(j)
print(capture2[1])
print(capture2[3])
