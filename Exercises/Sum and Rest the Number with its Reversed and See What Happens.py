def group_check(s):

	openings = ["{","[","("]
	closings = ["}","]",")"]
	openCount = 0
	closeCount = 0

	start = s[0]
	end = s[-1]

	check1 = False
	check2 = False

	for i in range(len(openings)):
		if start == openings[i] and end == closings[i]:
			check1 = True



	for i in s:
		if i in openings:
			openCount += 1
		if i in closings:
			closeCount += 1
	if openCount == closeCount:
		check2 = True

	if check1 == True and check2 == True:
		return True
	else:
		return False


assert group_check("{(})") == False
assert group_check("([]") == False
assert group_check("[])") == False
assert group_check("({") == False

assert group_check("({})") == True
assert group_check("[[]()]") == True
assert group_check("[{()}]") == True
assert group_check("()") == True







