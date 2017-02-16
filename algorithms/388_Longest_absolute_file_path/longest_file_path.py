#x = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
import timeit 
from collections import deque
import numpy as np
x = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
#x = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
#x = "dir\n\t        file.txt\n\tfile2.txt"
#x = "a"

def longest_path(s):
	stack = deque()
	level, length = 0, 0
	word = ""
	maxlen = 0
	for char in s:
		if char == '\n':
			if '.' in word:
				maxlen = max(maxlen, length + len(word))
			stack.append(len(word) + 1)
			length += len(word) + 1
			word = ""
			level = 0
		elif char == '\t':
			level += 1
		else:
			if not word:
				while len(stack) > level:
					length -= stack.pop()
			word += char
	if '.' in word:
		maxlen = max(maxlen, length + len(word))
	return maxlen

print longest_path(x)