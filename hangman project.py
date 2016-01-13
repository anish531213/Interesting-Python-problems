'''-----------------------------------------------------------
CS100 Project: Hangman, Part 1.

This single project is split into two sets of deliverables: Part 1 is
due November 22nd at 11:59 PM, and Part 2 is due December 4th at
11:59PM. This project is an individual (not group) assignment.

==Overview==
(For more information on the game Hangman, read about it on Wikipedia
(https://goo.gl/7boqSk) or play at http://goo.gl/VUXiBo. Your goal is to
complete the implementation of certain functions, which will be the building
blocks for creating a fully-functional version (text version, no graphical
interface) of Hangman later in Part 2 of this project.

==Instructions==
1. Everything in this entire file must be valid Python!
2. Do not change any pre-existing function names, but feel free to create
   new functions with their own unique names.
3. Implement your solutions by removing the pass keyword and writing your
   answer.
4. Sample function calls are provided, but your functions will be tested
   against a variety of values.
5. In order to submit on Blackboard, you'll probably need to paste all
   content in this Doc into a .py file (Python file) and submit that. You
   should be submitting only one file to Blackboard, which will contain
   implementations of all functions.
6. For more info on the pass keyword: http://goo.gl/rnA20w
7. See this doc for ideas on how to debug / diagnose your program:
   https://goo.gl/9WZGy9

==Grading==
1. Each question has equal worth.
2. Part 1 and Part 2 combined account for 15% of your total grade for CS100.
   There will be extra credit, available in Part 2.
3. Both the validity and styling of your solutions will be graded. Style
   guide: https://goo.gl/yMbtGJ
'''


'''-----------------------------------------------------------
Exercise 1:
Throughout play of Hangman, your program will display to the user
what letters in a word they've uncovered and what's still hidden.
This function should return back a new string where all hidden
letters are converted to an underscore.

Example:
answer --> 'welcome'
letters_guessed --> 'mel'
Return value --> '_el__me'

Notice that even though the user guessed 'e' once, all
occurrences of 'e' in the answer word are revealed to the user.
'''
def GetAnswerWithUnderscores(answer, letters_guessed):

    new = ''  #new is an empty string
    for i in answer:  #iterating through every letter in answer
        if i in letters_guessed:
            new += i
        else:
            new += '_'
    return new

answer = GetAnswerWithUnderscores('welcome', 'mel')
print('GetAnswerWithUnderscores #1: expected _el__me, got', answer)
answer = GetAnswerWithUnderscores('quick', 'rstlne')
print('GetAnswerWithUnderscores #2: expected _____, got', answer)


'''-----------------------------------------------------------
Exercise 2:
Take a look again at the Exercise 1's example. Notice how in some
fonts, it's difficult to visually differentiate between a single
underscore and two underscores next to each other? Write a function
that takes in a string and returns a new string with a single space
between each letter.
'''
def GetWordSeparatedBySpaces(word):

    #lets take a new list
    l = list(word)
    new = ' '.join(word)
    return new


answer = GetWordSeparatedBySpaces('plane')
print('GetWordSeparatedBySpaces #1: expected p l a n e, got', answer)
answer = GetWordSeparatedBySpaces('to')
# Don't worry about the hasattr function, the if statement, or what they
# do: it's not required for this Hangman assignment.
if hasattr(answer, 'strip') and answer.strip() == answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetWordSeparatedBySpaces #2: expected no spaces at the beginning or end,', text)


'''-----------------------------------------------------------
Exercise 3:
The user wins at Hangman once they've guessed all letters
in the answer word. This function should return True if
the user has won, and False otherwise.
'''
def IsWinner(answer, letters_guessed):

    for i in answer:
        if i not in letters_guessed:
            return False
    return True

answer = IsWinner('plane', 'ranedlp')
print('IsWinner #1: expected True, got', answer)
answer = IsWinner('plane', 'plan')
print('IsWinner #2: expected False, got', answer)


'''-----------------------------------------------------------
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


'''-----------------------------------------------------------
Exercise 6:
If the answer is 'welcome' and the user guesses 'c', this
helps the user win at Hangman. Write a function that returns
True if the user's guess reveals a letter in the answer, or False
if not. This function can assume the user's guess is legal.
'''
def IsGuessRevealing(answer, legal_letter_guess):

    if legal_letter_guess in answer:
        return True
    return False

answer = IsGuessRevealing('welcome', 'c')
print('IsGuessRevealing #1: expected True, got', answer)
answer = IsGuessRevealing('quick', 'z')
print('IsGuessRevealing #1: expected False, got', answer)


