import math as m


def mathFunc(x):
    return m.pow(3, x) / 2



for i in range(-10, 11):
    print(i, mathFunc(i))
