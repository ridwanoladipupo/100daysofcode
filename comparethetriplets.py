#HackerRank Challenge
#Compare the triplets

"""
Function Description:

Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.
compareTriplets has the following parameter(s):
a: an array of integers representing Alice's challenge rating
b: an array of integers representing Bob's challenge rating

"""

a = [17, 28, 30]
b = [99, 16, 8]

store_a = 0
store_b = 0

for i in range (len(a)):
    if a[i] > b[i]:
        store_a += 1

    if a[i] < b[i]:
        store_b += 1
            
compare = [store_a, store_b]

print("a's point : ", store_a)
print("b's point : ", store_b)
print(compare)
>>>>>>> fe3f6c6feee6003e3b4b3bd3b7542a58fd030dca
