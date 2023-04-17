def canSeePersonsCount(heights):
	# Length of the list
	n = len(heights)

	# Output list to return
	output = [0] * n

	# For each person
	for i in range(n):
		# We look at the right to find how many people he can see
		maxHeightOnRight = -1
		# Count of people ith person can see on right
		count = 0

		for j in range(i + 1, n):
			# A person can see another person on right
			if min(heights[i], heights[j]) > maxHeightOnRight: count += 1

			# Update the maximum height between i and j
			maxHeightOnRight = max(maxHeightOnRight, heights[j])

		# Update the count for "ith" person
		output[i] = count

	# Return the output list
	return output

heights = [10,6,8,5,11,9]
print("Output -> ", canSeePersonsCount(heights))