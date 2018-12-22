#Day [3/100]
#Sequence & Lists
#Slicing & Slicing list
#Method
#Tuple

#To demonstrate the knowledge of the above listed topic,
#I came up with a python program that captures 3 arrays: XYZ. Based on the captured element in the array,
#   find (1) minimum, maximum element in each of the arrays,
#        (2) match-sum the elements based on their corresponding position,
#        (3) maximum element of array XY combined,
#        (4) sort the combined XY
#        (5) reverse the sorted XY


X = []
Y = []
Z = []

matchsum = []

arraylength = int(input("Specify the length of array for capturing :"))

for i in range(arraylength):
     element = eval(input("Input the array element of X :"))
     X.append(element)
     
print("X =", X)
print("Minimum element of X =", min(X))
print("Maximum element of X =", max(X))

for i in range(arraylength):
     element = eval(input("Input the array element of Y :"))
     Y.append(element)
     
print("Y =", Y)
print("Minimum element of Y =", min(Y))
print("Maximum element of Y =", max(Y))

for i in range(arraylength):
     element = eval(input("Input the array element of Z :"))
     Z.append(element)
     
print("Z =", Z)
print("Minimum element of Z =", min(Z))
print("Maximum element of Z =", max(Z))

# Match-summing Array XYZ based on their corresponding position
for i in range(arraylength):
     add = X[i] + Y[i] + Z[i]
     matchsum.append(add)
     
print("Matchsum XYZ =", matchsum)

# Combining array element XY
X.extend(Y)

print("Combined - XY =", X)
print("Maximum element in the Combined - XY =", max(X))

# Sorting combined array XY
X.sort()
print("Sorted - XY =", X)

# Reversing sorted-combined array XY
X.reverse()
print("Reversed of sorted - XY =", X)

