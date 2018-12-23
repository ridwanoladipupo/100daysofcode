"""
Task 
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format
The first and only line contains the integer, .
Constraints
1 <= n <= 100

Output Format
Print n lines, one corresponding to each .
"""

if __name__ == '__main__':
    n = int(input(""))

for i in range(n):
    if((i *i) <= 100 ):
        i = i*i
        print(i)

