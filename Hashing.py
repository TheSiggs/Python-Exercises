t = [None for i in range(10)]

def Hash(x):
	h = x % 10
	return h

def store(x):
	h = Hash(x)
	t[h] = x
	print("{} stored in position {}".format(t[h], h))

store(29)