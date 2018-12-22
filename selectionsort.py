#Challenge : Selection sort


def selectionsort(nums):

    for i in range (5):
        minpos = i

        for j in range (i, 6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [7, 3, 8, 2, 5, 4]
selectionsort(nums)
print("Output : ", nums)

