# Gloabal variables
names = [
    {"Name": "Alexander Coder",
     "Nickname": "Allie",
     "phone": '027-356-5964',
     "address": "33 Kingston Drive"},

    {"Name": "Michael Jordan",
        "Nickname": "Mike",
        "phone": '021-456-3543',
        "address": "121 Chicago Lane"},

    {"Name": "Elaine Benes",
        "Nickname": "Elie",
        "phone": '021-555-1915',
        "address": "54 New York Street"},

    {"Name": "Tobias Fünke",
        "Nickname": "Toby",
        "phone": '06-555-6742',
        "address": "23 Beach Road"},
]


# Functions
def find():
    try:
        findNickname = input("Enter a Nickname: ")
        print()
        for contact in names:
            if contact["Nickname"].lower() == findNickname.lower():
                print("{0}\n{1}\n{3}\n{2}".format(
                    contact["Nickname"], contact["Name"],
                    contact["phone"], contact["address"]))
    except:
        print('There is nobody with the Nickname',
              findNickname, 'in the address book!')


def newEntry():
    while True:
        addNickname = input('Nickname: ')
        try:
            for contact in names:
                # Start of IF-ELSE
                if contact["Nickname"].lower() == addNickname.lower():
                    # If the nickname is taken
                    print('There is already a person with that Nickname')
                    sure = input(
                        'Would you like to replace the contact? Y/N: ')
                    if sure.upper() == 'Y':
                        # Prompt for information
                        names.remove(contact)
                        addName = input('Name: ')
                        addPhone = input('Phone: ')
                        addAddress = input('Address: ')
                        names.append({'Name': addName, 'Nickname': addNickname,
                                      'phone': addPhone, 'address': addAddress})
                        print(addNickname, 'has been added!')
                        restart = 2
                        break
                    else:
                        # Restart Script
                        restart = 1
                        break
        finally:
            if addNickname == '' or addNickname == ' ':
                # If the user entered nothing, exit the newEntry function
                break
            elif contact["Nickname"].lower() != addNickname.lower():
                # If the nickname isn't taken
                # Prompt for information
                addName = input('Name: ')
                addPhone = input('Phone: ')
                addAddress = input('Address: ')
                names.append({'Name': addName, 'Nickname': addNickname,
                              'phone': addPhone, 'address': addAddress})
                print(addNickname, 'has been added.')
                break
            elif restart != 1:
                break


def delete():
    try:
        findNickname = input("Enter a Nickname: ")
        found = 0
        print()
        for contact in names:
            if contact["Nickname"].lower() == findNickname.lower():
                found = 1
                print("{0}\n{1}\n{3}\n{2}".format(contact["Nickname"], contact[
                      "Name"], contact["phone"], contact["address"]))
                print('Is this the person you want to remove?')
                sure = input('Yes/No: ')
                if sure.lower() == 'yes' or sure.lower() == 'y':
                    names.remove(contact)
                    print()
                    print('Contact removed')
    finally:
        if found == 0:
            print('No Nickname Found')


def listAll():
    try:
        print("  {0:<15}{1:<20}{2:<20}{3:<20}".format(
            "Nickname:", "Name:", "Phone:", "Address:"))
        counter = 1
        for contact in names:
            print(counter, "{0:<15}{1:<20}{2:<20}{3:<20}".format(
                contact["Nickname"], contact["Name"],
                "(" + contact["phone"] + ")", contact["address"]))
            counter += 1
    except:
        print(end='')


def Quit():
    try:
        print('Quitting..')
        quit()
    except:
        print(end='')


def Menu():
    print('''
*** My Contacts ***
f - find
a - add new entry
d - delete
l - list all
q - quit
''')

# Main
while True:
    Menu()
    cmd = input('Commad: ')
    print()
    if cmd.lower() == 'f':
        find()
    elif cmd.lower() == 'a':
        newEntry()
    elif cmd.lower() == 'd':
        delete()
    elif cmd.lower() == 'l':
        listAll()
    elif cmd.lower() == 'q':
        Quit()
        break
    else:
        print('Invalid Command')
