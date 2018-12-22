# Revisiting function
# Challenge: Given an interger array arrayList of n elements and a search value (needle),
# write a function to search the value in arrayList. If search_ alue exists, then return true, otherwise return false

def search(arrayList, needle, arraySize):
    first = 0 
    last = arraySize - 1
    found = False
    while first <= last and not found:
        arrayCenter = (first + last)//2
        if arrayList[arrayCenter] == needle:
            found = True
        else:
            if needle < arrayList[arrayCenter]:
                last = arrayCenter - 1
            else:
                first = arrayCenter + 1
    return found
            
# defining array

print("Caution: Binary search algorithm works best with sorted list!")
size = int(input("Specify the array size: "))
items = []

# getting array elements

for i in range(size):
    items += [int(input("Enter next element: "))]

# get number to search for

needle = int(input("Enter the number to search for: "))
print("Initial Array = ",items)
print("Number = ",needle)
print("Search Result = ",search(items,needle,len(items)))
>>>>>>> fe3f6c6feee6003e3b4b3bd3b7542a58fd030dca
