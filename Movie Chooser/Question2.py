# ------------------------
#   Name: Sam Siggs
#     ID: 16059692
# -----------------------

# Imports
import random
# Variables
global favouriteMovies
lastMovie = []
favouriteMovies = []
# Functions

# Contols


def load():
    loadFile = str(input("Input File: "))
    try:
        if loadFile == '' or loadFile == ' ':
            file = open("movies.txt", "r")  # open the file
            movieList = file.readlines()  # load each line into a list
            file.close()  # close the file
            movieList = [movie.strip() for movie in movieList]
            print(len(movieList), "Movies loaded")
            return movieList

        else:
            file = open(loadFile, "r")  # open the file
            movieList = file.readlines()  # load each line into a list
            file.close()  # close the file
            # Creates a list out of the text file
            movieList = [movie.strip() for movie in movieList]
            print(len(movieList), "Movies loaded")
            return movieList  # returns list

    except:
        print('Invalid File')
        # movieList = load()


def amountLoaded():
    if len(movieList) == 1:
        print(len(movieList), "Movie loaded")
    elif len(movieList) > 1:
        print(len(movieList), "Movies loaded")
    else:
        print(len(movieList), "Movies loaded")


def Random():  # Picks a random title from the list.
    lastMovie.clear()  # clears last movie selected
    try:
        # Picks a random movie from the list
        randomMovie = random.choice(movieList)
        print()
        print("Your random movie is:", randomMovie)  # calls movie
        lastMovie.append(randomMovie)  # adds movie to your last movie

        return lastMovie  # returns last movie
    except:
        print('No file has been loaded')


def search():
    try:
        lastMovie.clear()  # clears last movie
        find = str(input("Movie Title: "))
        # Defines the input to be the first word of your search
        find = find.title()
        for i in range(len(movieList)):
            if find == '' or find == ' ':  # if the user inputs nothing

                print('No movies found!')
            # if the input matches something in the list
            elif find in movieList[i]:
                print(movieList[i], '\n')
                lastMovie.append(movieList[i])  # add it to last movie

    except:
        print('No movies found!')


def startsWith():
    try:
        lastMovie.clear()  # clears last movie
        findMovie = input("Type a letter: ")
        # Defines the input to be the first word of your search
        findMovie = findMovie.title()

        for i in movieList:
            if findMovie == '' or findMovie == ' ':
                print('No movie found')
                break
            elif i.startswith(findMovie):
                lastMovie.append(i)
                print(i)

    except:
        print('No movie found')


def keep():  # Stores the last title seen into the favouriteMovies array
    if len(lastMovie) == 1:
        favouriteMovies.append(lastMovie[0])
        print(lastMovie[0], 'has been added to your favourites')
    else:
        num = 0
        print('History')
        for i in lastMovie:
            print(num, '|', i)
            num += 1
        try:
            addToFav = int(input('Number assigned to movie (Enter Nothing to add the last movie in the list): '))
            print()
            favouriteMovies.append(lastMovie[addToFav])
            print(lastMovie[addToFav], 'Has been added')
        except:
            print('Invalid Movie')


# Displays the favouriteMovies array in a format that is readable
def favourites():
    if len(favouriteMovies) > 0:
        print('------------')
        print('Favourites')
        print('------------')
        print('\n'.join(favouriteMovies))

    else:
        print('You have nothing in your favourites')


def clear():  # Clears the favouriteMovies array
    if len(favouriteMovies) == 0:
        print()
        print('There is nothing in your favourites!')

    else:
        num = 0
        for i in favouriteMovies:
            print(num, '|', i)
            num = num + 1
        try:
            clearWhat = input(
                'What Movie do you want to clear? (Type all to clear all): ')

            if clearWhat == 'all':
                favouriteMovies.clear()
                print()
                print("Favourites cleared")
            try:
                clearWhat = int(clearWhat)
                print()
                print(favouriteMovies[clearWhat], 'has been removed')
                favouriteMovies.pop(clearWhat)
            except:
                print()

        except:
            print('Invalid Movie')


def Quit():  # Quits Program
    print("Quitting..")
    quit()


def Menu():  # Displays Menu
    print()
    print("------------------------------")
    print("l - load new file of movie titles")
    print("r - random movie")
    print("s - search")
    print("sw - starts with")
    print("k - keep - saves a displayed movie title to your favourites")
    print("f - display favourites")
    print("c - clear favourites")
    print("q - quit")
    print("------------------------------")


# Main
while True:
    print("*** Movie Title Explorer ***")
    print("l - load new file of movie titles")
    print("q - quit")
    command = input("Command: ")
    # if the user enters the command 'l', load all the movies into an array
    if command == 'l':
        movieList = load()
        break
    # if the user enters the command 'q', Quit the program
    elif command == 'q':
        Quit()
        break
    # if none of the commands match the if statements print 'Unknown Command'
    else:
        print("Unknown Command")


while True:  # Initialize
    Menu()
    command = input("Command: ")

    # if the user enters the command 'l', load all the movies into an array
    if command == 'l':
        movieList = load()

    # if the user enters the command 'r', pick a random movie from the movies
    # array
    elif command == 'r':
        Random()

    # if the user enters the command 's', goto the 'search()' function
    elif command == 's':
        search()

    # if the user enters the command 'sw', goto the 'startsWith()' function
    elif command == 'sw':
        startsWith()

    # if the user enters the command 'k', add the lastMovie into the
    # favouritesArray
    elif command == 'k':
        keep()

    # if the user enters the command 'f', display the favouriteMovies array
    elif command == 'f':
        favourites()

    # if the user enters the command 'c' clear the favouriteMovies array
    elif command == 'c':
        clear()

    # if the user enters the command 'q', Quit the program
    elif command == 'q':
        Quit()

    # if none of the commands match the if statements print 'Unknown Command'
    else:
        print("Unknown Command")
