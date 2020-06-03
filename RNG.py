import random
upper = float(input('Upper: '))
lower = float(input('Lower: '))
numOfTests = int(input('Number of tests: '))
print('--------------------')
for i in range(numOfTests):
    i += 1
    print(i, '%3s' % '|' + '%0.2f' % random.uniform(lower, upper))
