#Finding the Runner up score

n = int(input("Specify the length of array :"))
A = []

for i in range (n):
    element = int(input("Array element "))
    A.append(element)

print("A = ", A)

A.sort()

temp = A[-1]
print("Sorted list = ", A)

for i in range(n):
    if A[i] == temp:
        print ("2nd Runner Up :", A[i-1])
        break

