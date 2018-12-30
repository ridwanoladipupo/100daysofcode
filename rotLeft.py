"""
Check out the resources on the page's right side to learn more about arrays. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

A left rotation operation on an array shifts each of the array's elements 1
unit to the left. For example, if 4 left rotations are
performed on array [1,2,3,4,5], then the array would become [5,1,2,3,4].

Given an array 'a' of 'n' integers and a number, 'd' , perform 'd'

left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description:

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

- An array of integers 'a' .
- An integer, d the number of rotations.

"""


n = int(input("Specify the length of array :"))
rot = int(input("Specify the rotation :"))

lists = []

for i in range (n):
    element = int(input("Input the array element :"))
    lists.append(element)

print("List :", lists)

startIndex = lists.index(rot +1)

rotatedList = lists[startIndex : ] + lists[:rot]

resultantList = []
for x in rotatedList:
    print(x)
    resultantList.append(x)

print(resultantList)
