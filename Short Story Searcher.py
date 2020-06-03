# ------------------------
#   Name: Sam Siggs
#     ID: 16059692
# ------------------------

cmd = ''
stories = [
    ['With bloody hands, I say good-bye.', 'Frank Miller'],
    ['TIME MACHINE REACHES FUTURE!!! ... nobody there ...', 'Harry Harrison'],
    ['The baby\'s blood type? Human, mostly.', 'Orson Scott Card'],
    ['For sale: baby shoes, never worn.', 'Ernest Hemingway'],
    ['Corpse parts missing. Doctor buys yacht.', 'Margaret Atwood'],
    ['We kissed. She melted. Mop please!', 'James Patrick Kelly'],
    ['Starlet sex scandal. Giant squid involved.', 'Margaret Atwood'],
    ['Will this do (lazy writer asked)?', 'Ken McLeod'],
    ["Waking Up To Silence: Deafening silence. I strain my ears, praying there might be someone else still alive. The only noise I hear are the voices in my head",
        'Mike Jackson'],
    ["Not In My Job Description: Make sure it's done by the end of the day Jones. \nBut, sir, it's not in my .... \nJust do it, and remember, no blood.",
        'Mike Jackson'],
    ["Empty Baggage: The trunk arrived two days later. He lifted the lid and froze, it was empty. No arms, no legs, no head, nothing. Where was she?",
        'Mike Jackson'],
    ["Forgot My Own Name: The hospital said it was concussion. \nMight be permanent memory loss. \nCan\'t even remember my own name - which is handy considering who I am.",
        'Mike Jackson'],
    ["I\'m sorry, but there\'s not enough air in here for everyone. I\'ll tell them you were a hero.",
        'J. Matthew Zoss']
]


def menu():  # Displays menu
    print('''
s - search story
a - Dsiplays all stories by a author
sw - searches a certian word from a author
sl - Searches a story that has a certian amount of words
d - Displays all stories
q - quit program
''')


def search():
    word = input('Word: ')
    if len(word) == 1:
        print('There is no word in the list')
    elif len(word) > 1:
        for i in stories:
            for words in i[0:-1]:
                for author in i[1:13]:
                    if word in words:
                        print('"' + words + '"')
                        print('\t--', author, '\n')
    menu()


def displayAuthor():
    word = input('Word: ')
    if len(word) == 1:
        print('There is no word in the list')
    elif len(word) > 1:
        for i in stories:
            for words in i[0:-1]:
                for author in i[1:13]:
                    if word in author:
                        print('"' + words + '"')
                        print('\t--', author, '\n')
    menu()


def searchWord():
    word = input('Input word: ')
    author = input('Input author: ')

    if len(word) == 1:
        print('There is no word in the list')
    elif len(word) > 1:
        for i in stories:
            for words in i[0:-1]:
                if word in words:
                    for name in i[1:13]:
                        if author in name:
                            print('"' + words + '"')
                            print('\t--', name, '\n')

    menu()


def searchLimit():
    try:
        limit = int(input('Input Limit: '))
        counter = 0

        for author in stories:
            counter += 1
            for words in author[0:-1]:
                words = author[0].split()
                storyAuthor = author[1]
                if len(words) <= limit:
                    print('"' + ' '.join(words) + '"',
                          '\n \t -- ' + storyAuthor, end='\n\n')
                elif len(words) >= limit:
                    print(end='')
                    counter -= 1
        if counter == 0:
            print('No stories avliable')
        menu()
    except:
        print('Add a interger')
        menu()


def displayAll():
    try:
        for allStories in stories:
            for story in allStories[0:-1]:
                for author in allStories[1:13]:
                    print(story)
                    print('\t', '--' + author, '\n')
    finally:
        menu()


menu()
while True:  # Initialized
    cmd = input('Comand: ')
    if cmd == 's':
        search()
    elif cmd == 'a':
        displayAuthor()
    elif cmd == 'sw':
        searchWord()
    elif cmd == 'sl':
        searchLimit()
    elif cmd == 'd':
        displayAll()
    elif cmd == 'q':
        quit()
    else:
        print('invalid command')
