# Function
# Challenge : Bubble sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# to get the array size
arraySize = int(input("Please enter the size of the array: "))
arr = []

# to get the array element
for i in range(arraySize):
    arr += [int(input("Enter element {}: ".format(i+1)))]

print("\nInitial Array Elements: ", arr)
    
bubbleSort(arr)

print ("\nSorted array by bubble sort is: ", arr)
