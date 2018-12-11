# Revisiting function
# Challenge: Given an interger array arrayList of n elements and a target,
# write a function to search target in  

def bsearch(arrayList, i, r, search_value):
    if r >= 1:
        mid = int(i + (r -1)/2)

        if arrayList[mid] == search_value:
            return mid
        elif arrayList[mid] >= search_value:
            return bsearch(arrayList, i, mid - 1, search_value)
        else:
            return bsearch(arrayList, mid + 1, r, search_value)

    else:
        return -1

arrayList = [7, 3, 4, 9, 10]
x = 3

result = bsearch(arrayList, 0, len(arrayList) -1, x)
if result != -1:
    print("Element found at index ",  str(result))
else:
    print ("Element not found")
