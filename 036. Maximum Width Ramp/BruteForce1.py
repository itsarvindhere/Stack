def maxWidthRamp(nums):
    # Maximum Width of a ramp
	maxWidth = 0

	# Length of the list
	n = len(nums)

	# Go through each possible "i" value
	for i in range(n):
		# For each i value, check all possible j values
		for j in range(i + 1, n):
			# If it satisfies the condition, update the maxWidth if required
			if nums[i] <= nums[j]: maxWidth = max(maxWidth, j - i)

	# Return the maximum Width
	return maxWidth


nums = [6,0,8,2,1,5]

print("Maximum Width -> ", maxWidthRamp(nums))