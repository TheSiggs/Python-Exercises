# Imports
import random

# Global Variables
sentence = []

# The load() function below is extremely inefficient, tried to make it more
# efficent but sadly ran out of time.


def load():
    # Global Variables
    global adjectives, adverbs, conjunctions, transitives
    global intransitives, leadIns, nounMarker, nouns

    # Opens Adjectives.txt
    file = open('Adjectives.txt', 'r')
    adjectives = file.readlines()
    file.close()
    adjectives = [adjective.strip() for adjective in adjectives]

    # Opens Adverbs.txt
    file = open('Adverbs.txt', 'r')
    adverbs = file.readlines()
    file.close()
    adverbs = [adverb.strip() for adverb in adverbs]

    # Opens Conjunctions.txt
    file = open('Conjunctions.txt', 'r')
    conjunctions = file.readlines()
    file.close()
    conjunctions = [conjunction.strip() for conjunction in conjunctions]

    # Opens IntransitiveVerbs.txt
    file = open('IntransitiveVerbs.txt', 'r')
    intransitives = file.readlines()
    file.close()
    intransitives = [verbs.strip() for verbs in intransitives]

    # Opens Leadin.txt
    file = open('Leadin.txt', 'r')
    leadIns = file.readlines()
    file.close()
    leadIns = [lead.strip() for lead in leadIns]

    # Opens nounMarker.txt
    file = open('NounMarkers.txt', 'r')
    nounMarker = file.readlines()
    file.close()
    nounMarker = [nouns.strip() for nouns in nounMarker]

    # Opens Nouns.txt
    file = open('Nouns.txt', 'r')
    nouns = file.readlines()
    file.close()
    nouns = [nouns.strip() for nouns in nouns]

    # Opens TransitiveVerbs.txt
    file = open('TransitiveVerbs.txt', 'r')
    transitives = file.readlines()
    file.close()
    transitives = [verbs.strip() for verbs in transitives]


def testWords(adjectives, adverbs, conjunctions, intransitives,
              leadIns, nounMarker, nouns, transitives):
    # Prints all of the different word type examples
    print('''
-----------------------------------------
Adjective: {0}
Adverb: {1}
Conjunction: {2}
Intransitive Verb: {3}
Lead in: {4}
Noun Marker: {5}
Noun: {6}
Transitive Verb: {7}
'''.format(adjectives[0], adverbs[0], conjunctions[0],
           intransitives[0], leadIns[0], nounMarker[0],
           nouns[0], transitives[0]))


def easySentence(intransitives, nouns):
    firstWord = random.choice(nouns)
    firstWord = firstWord.capitalize()
    secondWord = random.choice(intransitives)
    print()
    print(firstWord, secondWord + '.')


def nounPhrase(nounMarker, adjectives, nouns):
    nounMarker = random.choice(nounMarker)
    nounMarker = nounMarker.capitalize()
    sentence.append(nounMarker)
    if random.choice([0, 1]) == 0:
        adjective = random.choice(adjectives)
        sentence.append(adjective)
    # random noun
    noun = random.choice(nouns)
    sentence.append(noun)


def verbPhrase(transitives, intransitives, nounMarker):
    if random.choice([0, 1]) == 0:
        transitiveVerb = random.choice(transitives)
        sentence.append(transitiveVerb)
        nounMarker = random.choice(nounMarker)
        sentence.append(nounMarker)
        if random.choice([0, 1]) == 0:
            adjective = random.choice(adjectives)
            sentence.append(adjective)
        # random noun
        noun = random.choice(nouns)
        sentence.append(noun)

    else:
        intransitiveVerb = random.choice(intransitives)
        sentence.append(intransitiveVerb)


def newSentence(sentence, adjectives, adverbs, conjunctions,
                intransitives, leadIns, nounMarker, nouns, transitives):
    sentence.clear()  # Clears sentance
    # Part One
    # Lead in
    if random.choice([0, 1]) == 0:
        lead = random.choice(leadIns)
        lead = lead.capitalize()
        sentence.append(lead)

    # Part Two
    # Noun
    nounPhrase(nounMarker, adjectives, nouns)

    # Part Three
    # Adverb
    if random.choice([0, 1]) == 0:
        adverb = random.choice(adverbs)
        sentence.append(adverb)

    # Part Four
    # Verb
    verbPhrase(transitives, intransitives, nounMarker)

    # Finally prints the sentance
    print('{0}.'.format(' '.join(sentence)))


def Quit():
    try:
        print('Have a nice day, Goodbye!\nQuitting...')
        quit()
    except:
        print(end='')


def startUp():
    prompt = '''
-----------------------------------------
        Sentence Generator Loader
-----------------------------------------
L - Load all the files of words from disk
Q - Quit the program
CMD: '''
    cmd = input(prompt)
    if cmd.upper() == 'L':
        load()
    elif cmd.upper() == 'Q':
        Quit()
    elif cmd.upper() == '':
        print('Error: no command entered!')
        startUp()
    else:
        print('Error: {0} is not a valid command!'.format(cmd))
        startUp()

# Menu
startUp()
while True:
    prompt = '''
-----------------------------------------
            Sentence Generator
-----------------------------------------
L - Load all the files of words from disk
T - Test Words
E - Easy Sentence
S - New Sentence
Q - Quit the program
CMD: '''

    cmd = input(prompt)
    if cmd == 'L' or cmd == 'l':
        load()
    elif cmd.upper() == 'T':
        testWords(adjectives, adverbs, conjunctions, intransitives,
                  leadIns, nounMarker, nouns, transitives)
    elif cmd.upper() == 'E':
        easySentence(intransitives, nouns)
    elif cmd.upper() == 'S':
        newSentence(sentence, adjectives, adverbs, conjunctions,
                    intransitives, leadIns, nounMarker, nouns, transitives)
    elif cmd.upper() == 'Q':
        Quit()
    elif cmd.upper() == '':
        print('Error: no command entered!')

    else:
        print('Error: {0} is not a valid command!'.format(cmd))
