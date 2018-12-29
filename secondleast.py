#Finding the Second least in a list

n = int(input("Specify the length of array :"))
A = []

for i in range (n):
    element = int(input("Array element "))
    A.append(element)

print("A = ", A)

A.sort()

print("Sorted list = ", A)

temp = A[0]

for i in range(n):
    if A[i] == temp:
        print ("2nd Least :", A[i+1])
        break

