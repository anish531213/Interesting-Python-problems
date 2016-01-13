'''
Exercise 4:
When playing Hangman, a user should be guessing one unique
letter at a time: let's call those 'legal guesses'. When a
user guesses a number, symbol, or two-letter guess, let's
call those 'illegal guesses'. Based on the newly guessed
letter and a string of all previously guessed letters,
write a function that returns True if the newly guessed
letter is legal. If the guess is illegal, print why the guess
is illegal and return False.
'''
def IsLegalGuess(current_guess, letters_guessed):

    if type(current_guess) != str:
        print('your guess is not a string')
        return False
    else:
        if not current_guess.isalpha():
            print('your guess is not a valid string')
            return False
        else:
            if len(current_guess) > 1:
                print('you should guess a single letter')
                return False
            else:
                if current_guess in letters_guessed:
                    print('you have already guessed this letter')
                    return False
                else:
                    return True

answer = IsLegalGuess('g', '')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('g', 'rstle')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('bb', 'cat')
print('IsLegalGuess #1: expected False, got', answer)
answer = IsLegalGuess('p', 'yzpr')
print('IsLegalGuess #1: expected False, got', answer)


'''-----------------------------------------------------------
Exercise 5:
As the user plays Hangman, the program should ask for a
new letter to guess. This function should prompt the user
for a letter using the 'input' function. If the guess
is not legal (hint: use your IsLegalGuess function), ask again
for a new letter. Only after the user makes a legal guess
should this function return the legal guess.

Example:
1. letters_guessed --> 'abc'
2. Program asks user for a letter
3. User types in 'c'
4. The program should state to only make unique guesses and
   prompt again for a letter
5. Program asks user for a letter
6. User types in 'd'
7. Since this is a legal guess, the function should return 'd'
'''
def GetLegalGuess(letters_guessed):
    guess = input("letter: ")
    while not IsLegalGuess(guess, letters_guessed):
        guess = input("letter: ")
    return guess
    
print('GetLegalGuess: Test this yourself using the example above')
print(GetLegalGuess('abc'))
