#Challenge : Number Permutation

def permutation(items):
    if len(items) == 1:
        return [items]
    permutations = []
    for i in range(len(items)):
        m = items[i]
        remItems = items[:i] + items[i+1:]
    #Generating all permutations
        for p in permutation(remItems):
            permutations.append([m] + p)
    return permutations

#Define list
size = int(input("Enter list size: "))
items = []
for i in range(size):
           items += [int(input("Enter next item: "))]
print("Initial items = ", items)
permutations = permutation(items)
print("Permutations: ")
for i in range(len(permutations)):
    print(permutations[i])
