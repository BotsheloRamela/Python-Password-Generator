import string
import secrets

def getPasswordLength():
    """Get password length from user"""

    passwordLength = int(input('>> Choose a password length between 4-12. '))

    if passwordLength not in range(4, 13):
        print('Password length is not accepted.')
        passwordLength = int(input('Choose a password length between 4-12. '))
    
    return passwordLength


def passwordCreator(passwordLength, passwordType):
    """Create a specific password type"""

    password = ''

    for i in range(passwordLength):
        password += ''.join(secrets.choice(passwordType))
        
    return password


def generateMixedPassword():
    """Generate a random mixed password"""

    letters = string.ascii_letters
    digits = string.digits
    specialDigits = string.punctuation

    alphabet = letters + digits + specialDigits
    passwordLength = getPasswordLength()
    
    password = passwordCreator(passwordLength, alphabet)

    print(f'\nMixed password generated!\nPassword: {password}\n')


def generateLetterPassword():
    """Generate a letter only random password"""

    letters = string.ascii_letters
    passwordLength = getPasswordLength()

    password = passwordCreator(passwordLength, letters)

    print(f'\nLetter only password generated!\nPassword: {password}\n')


def generateSpecialDigitPassword():
    """Generate a digit only password"""

    digits = string.digits
    specialDigits = string.punctuation

    alphabet = digits + specialDigits
    passwordLength = getPasswordLength()

    password = passwordCreator(passwordLength, alphabet)

    print(f'\nSpecial digit password generated!\nPassword: {password}\n')


def helpMenu():
    """Returns a menu of valid commands"""

    print("""VALID COMMANDS:
    HELP > Get help menu
    DIGIT-ONLY > Generate a special digit only password
    LETTERS-ONLY > Generate a letters only password
    MIXED > Generate a mixed password
    OFF > Shut down the program
    """)


def getUserInput():
    """Get user input"""
    return input('>> What can I do for you? ')


def main():
    
    validCommands = ['HELP', 'DIGIT-ONLY', 'LETTERS-ONLY', 'MIXED', 'OFF']

    print('Welcome to Random Password Generator!\nRun the HELP command to get assistance.\n')
    
    userInput = getUserInput()

    while True:
        if userInput.upper() in validCommands:
            if userInput.upper() == validCommands[0]:
                helpMenu()
                userInput = getUserInput()

            elif userInput.upper() == validCommands[1]:
                generateSpecialDigitPassword()
                userInput = getUserInput()
            
            elif userInput.upper() == validCommands[2]:
                generateLetterPassword()
                userInput = getUserInput()

            elif userInput.upper() == validCommands[3]:
                generateMixedPassword()
                userInput = getUserInput()
            
            elif userInput.upper() == validCommands[4]:
                print('Goodbye!')
                break

        else:
            print('Not a valid command, try again.\n')
            userInput = getUserInput()


if __name__ == '__main__':
    main()