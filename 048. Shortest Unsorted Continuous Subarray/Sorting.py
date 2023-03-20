def findUnsortedSubarray(nums) -> int:
	# Length of the input list
	n = len(nums)

	# The Sorting approach is pretty simple
	# We will sort the given list but also keep the original indices
	nums = [(num,i) for i,num in enumerate(nums)]

	nums.sort()

	# Now, once we get the sorted list, we just want to find the first index
	# such that the element at that index was not present at the same index in original unsorted list
	# That would be the beginning of our unsorted part

	# For example, if we have     [1,3,2,4]
	# Then if we sort it, we get  [1,2,3,4]

	# Here we see that "1" and "4" are at the same place as in original array
	# But "3" and "2" are not at the same place. It means, the part [3,2] is the unsorted part

	# Find the beginning of the unsorted subarray
	i = 0
	while i < n and i == nums[i][1]: i += 1

	# And same thing we will do to get the end of the unsorted part

	# Find the end of the unsorted subarray
	j = n - 1
	while j >= i and j == nums[j][1]: j -= 1

	# And finally, the count of elements between i and j (both inclusive) 
	# is the required length of the shortest unsorted subarray which, if sorted, will sort the entire list
	return j - i + 1


nums = [2,6,4,8,10,9,15]

print("Length of shortest unsorted subarray is -> ", findUnsortedSubarray(nums))