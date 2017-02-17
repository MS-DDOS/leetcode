x = "aabcccccaaa"
x = "abcdefg"
x = "aabcbefejejwwjwwwkkkeennncagjhgwejnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
from collections import deque

def compress(raw_string):
	stack = deque()
	output = ""
	for char in raw_string:
		if len(stack) > 0:
			if char == stack[-1]: # if char == stack.peek()
				stack.append(char)
			else:
				output += "{:}{:}".format(stack[-1],len(stack))
				stack = deque()
				stack.append(char)
		else:
			stack.append(char)
	if stack:
		output += "{:}{:}".format(stack[-1],len(stack))
	if len(output) > len(raw_string):
		return raw_string
	return output

print compress(x)

