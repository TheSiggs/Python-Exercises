# ---------
# Problem 1
# --------- 
# Opens file
file = open('prob1.in', 'r')
Q1List = file.readlines()
file.close()
# Puts everything from file into a list and lays out list properly
Q1List = [number.strip() for number in Q1List]
Q1List = [num.split(" ") for num in Q1List]
Q1List = sum(Q1List, [])

def sortList(unsortedList):
	unsortedList = list(set(unsortedList)) # Removes duplicates from unsorted list
	sortedList = []
	while unsortedList:
		minimum = unsortedList[0]
		for x in unsortedList:
			if x < minimum: # Check to see if the next value in the list is less than the current minimum value
				minimum = x # x is new minimum
		sortedList.append(minimum) # append it to a new list
		unsortedList.remove(minimum) # remove from unsorted list
	return " ".join(sortedList)

# Adds string to file
with open("prob1.out", "w") as output:
	output.write(sortList(Q1List))
output.close()


# ---------
# Problem 2
# --------- 
import itertools

# Opens and reads file
file = open('prob2.in', 'r')
Q2List = file.readlines()
file.close()
Q2List = [number.strip() for number in Q2List] # Puts everything from file into a list and lays out list properly
Q2List = [num.split(" ") for num in Q2List]
listofWords = Q2List[1:-1] # removes numbers from the list so only words remain
Q2List = sum(Q2List, [])

dictWords = {}
numpad = {"a":"2", "b":"2", "c":"2", "d":"3", "e":"3", "f":"3", "g":"4", "h":"4", "i":"4", "j":"5", "k":"5", "l":"5", "m":"6", 
		  "n":"6", "o":"6", "p":"7", "q":"7", "r":"7", "s":"7", "t":"8", "u":"8", "v":"8", "w":"9", "x":"9", "y":"9", "z":"9"}

for word in listofWords: # Makes a dictionary out of all of the words given in the text file
	letters = [letter for currentWord in word for letter in currentWord] # makes a list of letters. currentWord removes word from the word list
	num = "".join(numpad.get(num,num) for num in letters) # turns all of the letters into numbers from the numpad dictionary
	dictWords.update({word[0]: num}) # adds num to dictWord as a key value pair of the word and it's number

compareMe = Q2List[-1] # String of numbers in the text file that everything needs to be compared to
Combinations = Q2List[1:-1]# Gets all of the words from file
convertedList = [dictWords.get(num,num) for num in Combinations] # Changes every word into a number form
listOfCombinations = [list(itertools.product(convertedList, repeat=indx)) for indx in range(len(convertedList)*2)] # List of every possible combinations
listOfCombinations = ["".join(combination) for Set in listOfCombinations for combination in Set] # Joins the sets into a string
matches = sum(1 for match in listOfCombinations if match == compareMe) # Number of matches made

# Adds number of matches to new file
with open("prob2.out", "w") as output:
	output.write(str(matches))
output.close()


# ---------
# Problem 3
# --------- 
file = open('prob3.in', 'r')
listOfNumbers = file.readlines()
file.close()
listOfNumbers = [number.strip() for number in listOfNumbers] # Puts everything from file into a list and lays out list properly

def makeDict(elements, Dict={}): # creates a dictionary out of a given list
	for indx in elements[1:]:
		keyValue = []
		for element in indx:
			if element != ' ':
				keyValue.append(element)
		Dict.update({keyValue[0]: keyValue[1]})
	return Dict # Returns a dictionary

def cyclic(graph):
    path = set() # Set for visit() to add to so it doesn't clash with visited
    visited = set() # Set for visit() to add to from path

    def visit(vertex):
        if vertex in visited:
            return False # There is a Cycle
        # Keep track of the visited nodes
        visited.add(vertex) # Add vertex to visited
        path.add(vertex) # Add vertex to path
        for neighbour in graph.get(vertex, ()):
        	# If neighbour has been to a node before
	        if neighbour in path or visit(neighbour):
	            return True # Cycle here!
        path.remove(vertex) # Refresh path for next iteration
        return False # No cycles here!
    return any(visit(vertex) for vertex in graph) # Return boolean 


graph = makeDict(listOfNumbers) # Creates a dictionary from listOfNumbers
findCycle = cyclic(graph) # Gives a boolean value to see if there is a cycle or not
secondVertcicies = [branch[-1] for branch in listOfNumbers[1:]] # Adds all of the second vertices's to a separate list

# If a vertex comes up more than once in the graph or if a cycle has been found it's not a tree
if len(secondVertcicies) != len(set(secondVertcicies)) or findCycle == True:
	tree = "is not"
else: # Otherwise it's a tree
	tree = "is"

with open("prob3.out", "w") as output: # Adds "tree" to file
	output.write(str("this {} a tree".format(tree)))
output.close()