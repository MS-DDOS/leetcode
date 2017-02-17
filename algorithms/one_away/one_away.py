tests = [("pale", "ple"), ("zale","zales"), ("pale", "bale"), ("pale","bake")]

def one_away(input_string, comparison_string):
	if abs(len(input_string) - len(comparison_string)) > 1:
		return False

	loffset = 0
	roffset = 0
	incorrect = False
	for i in range(min(len(input_string), len(comparison_string))):
		if input_string[i + loffset] != comparison_string[i + roffset]:
			if len(input_string) < len(comparison_string):
				loffset -= 1
			elif len(input_string) > len(comparison_string):
				roffset -= 1
			if incorrect:
				return False
			else:
				incorrect = True
		if incorrect and input_string[-1] != comparison_string[-1]:
			return False
	return True




for test in tests:
	print one_away(test[0], test[1])