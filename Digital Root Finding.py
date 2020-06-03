def digital_root(n):
	n = str(n)
	strnum = [int(num) for num in n]
	num = sum(strnum)
	if len(str(num)) > 1:
		digital_root(num)
	else:
		print(num)
		return num

digital_root(493193)