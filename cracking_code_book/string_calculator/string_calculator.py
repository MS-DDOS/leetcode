
augend = "123"
addend = "123"
true_sum = int(augend) + int(addend) #152

multiplicand = "13"
multiplier = "14"
true_product = int(multiplicand) * int(multiplier)

def string_add(augend, addend):
	from collections import deque
	if len(augend) == 0:
		return addend
	elif len(addend) == 0:
		return augend
	elif len(addend) == 0 and len(augend) == 0:
		return "0"
	carry = 0
	accumulator = deque()
	if len(augend) > len(addend):
		augend = deque(augend)
		addend = deque(addend)
	else:
		temp = augend
		augend = deque(addend)
		addend = deque(temp)
	while augend:
		if addend:
			val = int(augend.pop()) + int(addend.pop()) + carry
		else:
			val = int(augend.pop()) + carry

		carry = 0

		if val > 9:
			carry = 1
			accumulator.appendleft(str(val % 10))
		else:
			accumulator.appendleft(str(val))
	return "".join(accumulator)

def string_mult(multiplicand, multiplier):
	if len(multiplicand) == 0 or len(multiplier) == 0:
		return "0"
	from collections import deque
	carry = 0
	committed = ""
	accumulator = deque()
	multiplier = deque(multiplier)
	multiplicand = deque(multiplicand)
	for i in xrange(len(multiplier)-1,-1,-1):
		for j in xrange(len(multiplicand)-1, -1, -1):
			val = (int(multiplier[i]) * int(multiplicand[j])) + carry # largest possible value is 81 + 9 = 90
			carry = 0
			if val > 9:
				carry = int(str(val)[0])
				accumulator.appendleft(str(val)[1])
			else:
				accumulator.appendleft(str(val))
		committed = string_add(committed, "".join(accumulator))
		accumulator = deque([str(0) for _ in xrange(len(multiplier)-i)])
	return committed
print "Calc:", string_add(augend, addend), "True:", true_sum
print "Calc:", string_mult(multiplicand, multiplier), "True:", true_product