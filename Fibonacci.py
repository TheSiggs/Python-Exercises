# Method 1 with iteration
def fib(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Method 2 without iteration
def fib2(n):
    if n == 1:
        return 1
    else:
        res = n * fib2(n - 1)
        return res


def fib3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib4(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib5(a, memo={0: 1, 1: 1}):
    if a in cache:
        return memo[a]
    res = fib(a - 1, memo) + fib(a - 2, memo)
    memo[a] = res
    return res

def fib_bottom_up(a, val1=0, val2=1):
    result = 0
    for x in range(a):
        result = val1 + val2
        val1 = val2
        val2 = result
    return result

print(fib_bottom_up(100000))