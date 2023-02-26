def simplifyPath(path: str) -> str:
	# Length of the input path
	n = len(path)

	# Stack that we will use to construct the path
	stack = ["/"]

	i = 1
	while i < n:

		# If we get a dot
		if path[i] == ".":
			# If there are more than 2 dots together, they represent a file
			countOfDots = 0
			while i < n and path[i] == ".":
				countOfDots += 1
				i += 1

			# Are these dots in a file's name?
			# In that case, we have to consider them

			# What are the conditions for dots to be in a file'a name?
			# 1. They are present between the characters. e.g. "Hello...World"
			condition1 = stack[-1] != "/"

			#2. They are present in the beginning of the characters. e.g. "...Hello"
			condition2 = i < n and path[i] != "/"


			#3. They are present after the characters e.g. "Hello..."
			# Same as condition 1

			# 4. The file name is simply all dots
			condition3 = countOfDots > 2

			isFileName = condition1 or condition2 or condition3

			if isFileName: 
				dotString = "." * countOfDots
				if condition1: stack.append(dotString)
				else: stack[-1] += dotString


			# If there are double dots, it means go one level up
			if countOfDots == 2 and not isFileName:
				# If we are not at the root directory already
				if len(stack) != 1:

					# Remove the previous slash first
					stack.pop()

					# Then remove the previous directory
					stack.pop()


		# If we get a slash
		elif path[i] == "/":

			# Skip all the slashes that are together
			while i < n and path[i] == "/": i += 1

			# We will only put it in stack is we don't already have a slash before it
			# Since multiple consecutive slashes are treated as single slash
			if stack[-1] != "/": stack.append("/")

		# For file or directory names
		else:
			if stack[-1] == "/": stack.append(path[i])
			else: stack[-1] += path[i]

			i += 1


	# Don't forget to remove the last slash
	if len(stack) > 1 and stack[-1] == "/": stack.pop()

	return "".join(stack)


path = "/a/./b/../../c/"

print("Simplified Path -> ", simplifyPath(path))