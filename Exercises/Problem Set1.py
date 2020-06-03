
# -------------
# Problem Set 1
# -------------


# Q1
def sum_list(alist):
    sum = 0
    for i in alist:
        sum += i
    return sum

mylist = [45, 2, 10, 45, 100]
print(sum_list(mylist))
print()


# Q2
def get_user_choice():
    while True:
        command = input("Command: ")
        if command == 'f' or command == 'm' or command == 's' or command == 'd' or command == 'q':
            return command

        print("Hey, that's not a command. Here are your options:")
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")

user_command = get_user_choice()
print("You entered: " + user_command)
print()


# Q3
def reverse(text):
    result = ""
    text_split = list(text)
    text_split.reverse()
    for i in text_split:
        result += i
    return result

text = "Programming is the coolest thing ever."
print(reverse(text))
print()


# -------------
# Problem Set 2
# -------------


# Q1
for i in range(6):
    for j in range(10):
        print(j, '', end='')
    print()
    if i < 5:
        print("%10s" % '0')
print()


# Q2
s = 0
for i in range(10, 0, -1):
    print(" " * s, end="")
    for j in range(i):
        print("{0:>1} ".format(j), end="")
    s += 2
    print()
print()


# -------------
# Problem Set 3
# -------------


# Q1
def chop(mylist):
    mylist.pop(0)
    mylist.pop(-1)
    return mylist

mylist = [1, 3, 4, 5, 6, 7]
print(mylist)
chop(mylist)
print(mylist)
print(chop(mylist))
print()


# Q2
def evens(mylist):
    result = []
    for n, i in enumerate(mylist):
        if n % 2 == 0:
            result.append(i)
    return result

print(evens([["me", "my"], ["you", "yours"], ["them"], ["their"], ["theirs"]]))
print()


# Q3
def is_abecedarian(string):
    split_string = list(string)
    while True:
        word1, word2, i = '', '', 0
        word1, word2 = split_string[i], split_string[i + 1]
        if word1 < word2:
            return True
        else:
            return False

words = ["loop", "baby", "loops", "looping", "loopy"]
for i in words:
    print(is_abecedarian(i))
print()


# Problem Set 4
# Q1
def square_list():
    return [n for n in range(0, 99) if n % 2 == 0 and (n**0.5) % 1 == 0]
print(square_list())
print()


# Q2
def wordlengths(mywords):
    return [(i.upper(), len(i)) for i in mywords]

print(wordlengths(["The", "quick", "brown", "fox"]))
