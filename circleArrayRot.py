# https://www.hackerrank.com/challenges/circular-array-rotation/problem?h_r=internal-search

lists = [1, 2, 3]
k = 2
m = [1,2]

rot1 = lists[-1]
rot2 = lists[0]

print("List :", lists)

startIndex = lists.index(rot1)
SecondIteration = lists.index(rot2)

Firstrot = lists[startIndex : ] + lists[:rot1 -1]
Secondrot = lists[SecondIteration : ] + lists[:rot2 -1]

firstrotList = []
resultantList = []

for x in Firstrot:
    print(x)
    firstrotList.append(x)

print(firstrotList)

for x in Secondrot:
    print(x)
    resultantList.append(x)

print(resultantList)

print("m = [1] :", resultantList[1])
print("m = [2] :", resultantList[2])
