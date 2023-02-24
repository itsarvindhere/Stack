def calculate(s: str) -> int:
	# Length of the input string
	n = len(s)

	# Stack that we will use for calculations
	stack = []

	# Set of operators
	operators = {"+", "-", "/", "*"}

	# Main Loop starts
	i = 0

	while i < n: 

		# If it is a space, we will ignore and move to next character
		if s[i] == " ": 
			i += 1
			continue

		# Otherwise, if it is a number
		elif s[i] not in operators: 

			# Get the current number
			# Since a number can have multiple digits
			# We want to capture the whole number before doing any calculations
			# This won't affect the complexity since we won't go over all these indices (i) again
			c = 0  
			while i < n and s[i] not in operators and s[i] != " ": 
				c = (c * 10) + int(s[i])
				i += 1

			# Once we get the number, now we will check if stack is empty or not
			# If it has some values, it means, there is at least one number and one operator in the stack
			if stack:

				# We take out the operator first
				operator = stack.pop() 

				# If it is a "+" operator, we don't do anything and simply push the current number to stack
				# Why? Because what if there are multiplication and division operations after it?
				# If we calculate the sum here, our final calculation might not be correct
				# In simple words, we will first do all the multiplication and division operations
				# And only after that we will do the addition and substraction
				if operator == "+": stack.append(c)

				# If it is a "-" operator, we will again push the current value to stack but in negative
				elif operator == "-": stack.append(-c)

				# If it is "*" operation, we will multiple current number with previous number in stack
				# And then replace the previous number with this new result that we get after multiplication
				elif operator == "*": stack[-1] *= c

				# If it is "/" operation, we will divide current number and previous number in stack
				# And then replace the previous number with this new result that we get after division
				# Do note that "integer division should truncate toward zero."
				else: stack[-1] = int(stack[-1] / c)     


			# If stack is empty, simply push current number to the stack
			else: stack.append(c)

		# If it is an operator, then push it to the stack as well
		else: 
			stack.append(s[i])
			i += 1

	# Finally, the sum of all values in our stack will give us the required output
	return sum(stack)


s = "1*2-3/4+5*6-7*8+9/10"
print("Output -> ", calculate(s))