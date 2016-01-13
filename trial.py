import os
import random

'''-----------------------------------------------------------
CS100 Project: Hangman, Part 2. Due December 6th at 11:59PM.

==Overview==
The overview is in the Part 1 document:
https://docs.google.com/document/d/1qGJv7-8hS78vKRjcM_3XCTJV8NRWpseWGlmFqvBxiyE/edit .

==Instructions==
1. Everything in this entire file must be valid Python!
2. Do not change any pre-existing function names, but feel free to create
   new functions with their own unique names.
3. Implement your solutions by removing the pass keyword and writing your
   answer.
4. Sample function calls are provided, but your functions will be tested
   against a variety of values.
5. In order to submit on Blackboard, you'll need to paste all content from
   this Doc into a .py file (Python file) and submit that. You should be
   submitting only one file to Blackboard, which will contain
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
Copy & paste all your functions from your Project's Part 1.
'''
#project 1 pasted
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

#project 1 end


'''-----------------------------------------------------------
Exercise 2:
In order to play Hangman, the computer needs access to a list of
all English words for possible answers to Hangman. Write a function
that reads from a file called 'hangman_english_words.txt' (see below)
and returns a list of all English words.

Download https://goo.gl/45eP4p (this is the
'hangman_english_words.txt' file) and put in the same directory
as this Hangman Python file.

For documentation on reading a file in a Python program, read
Chapter 9 in the book. We will not be covering this chapter in class.
Hint: if you're encountering a problematic \n character when reading
words from the file, try help(str.strip)

DISCLAIMER! I downloaded this file from the Internet, which was
apparently compiled from Google's Trillion Word Corpus. I did not
go through all 6,394 words; as such, I have no idea if there are
any offensive words in this list. Apologies in advance, and if you
find any offensive words, email me and I'll remove it.
'''
def GetAllEnglishWords():
    f = open('hangman_english_words.txt')
    z = []
    for a in f:
        z.append(a.strip())
    f.close()
    return z


answer = GetAllEnglishWords()
if answer != None and 'voting' in answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetAllEnglishWords #1: expected the word voting', text)
if answer != None and 'triage' not in answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetAllEnglishWords #2: did not expect triage', text)


'''-----------------------------------------------------------
Exercise 3:
Write a function that takes in a list as a parameter and returns
one of the elements at random.
'''
def GetRandomWord(words):
    # taking a random number from among total number of string in the list
    r = random.randint(0, len(answer)-1)
    return (GetAllEnglishWords()[r])


words = ['train', 'plane', 'automobile']
answer = GetRandomWord(words)
print('GetRandomWord #1: expected a random word,', answer in words)


'''-----------------------------------------------------------
Exercise 4:
(Read Exercise 5 before attempting this exercise, to understand what
these two functions should be doing.)

This function takes in the Hangman word as a parameter. It should
continuously ask the user for a letter to guess and process it. It
should also return True if the user won and False if the user lost.
* If the guess uncovers a new letter in the answer, print something
  positive.
* If the guess uncovers the last remaining letter, tell the user
  they've won.
* If the guess does not help, print that the guess does not help.
* If this is the player's 5th time making an incorrect guess (in
  other words, if the player has 5 strikes),  then the user has
  lost.
See below for example text that's displayed as the user plays.

You have 0 strikes.
_ _ _ _ _ _ _ _
Guess: O
Good guess! Continue.
_ O _ _ _ O _ _
Guess: E
E is not in the word. You have 1 strike.
_ O _ _ _ O _ _
Guess: O
You have already guessed O. Try again.
_ O _ _ _ O _ _
Guess: Z
Z is not in the word. You have 2 strikes.
_ O _ _ _ O _ _
Guess: A
Good guess! Continue.
_ O _ A _ O _ _
Guess: 

Notice that it's good to display the underscores and letters
discovered pretty often while playing, so the user knows
what's left. Also notice that illegal guesses, such as guessing
a letter that the user has already guessed, do not result
in a strike.
'''
def Play(answer):
    print(answer)
    z = '123'
    strike = 0
    letters_guessed = ''
    while strike < 5 and not IsWinner(answer, letters_guessed):
        if z in answer:
            print("Goog guess! Try more")
        else:
            print("You have ", strike, " strikes")
        z = GetLegalGuess(letters_guessed)
        letters_guessed += z
        if z not in answer:
            strike += 1
        print(GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, z+letters_guessed)))
        
    if IsWinner(answer, letters_guessed):
        return "WOW, YOU WIN"
    return "Sorry, You Lose"


'''-----------------------------------------------------------
Exercise 5:
This should be a very simple function, as most of it is just
using all of the other functions you've created. Get all English
words, pick an answer at random, and call Play(...) with the
answer word. This function should also allow the user to
continuously play Hangman by prompting, "Do you want to play
again?"
'''
def StartupAndPlay():
    print(Play(GetRandomWord(words)))
    ask = input("Do you want to play again?(y/n)")
    if ask == 'y':
        StartupAndPlay()


'''-----------------------------------------------------------
Exercise 6:
So far, whenever we've created a function inside of a script, we just
write a function call to use it. There's a more correct way to call
functions inside of a script.
* This page contains the code you'll need: https://goo.gl/9vebJU
* This page explains the code: http://goo.gl/JkGHX2
'''
##def main():
##    StartupAndPlay()
##    
##if __name__ == "__main__":
##    # execute only if run as a script
##    main()



'''-----------------------------------------------------------
Extra credit exercise 1:
General announcement: these extra credit exercises are about
recording and displaying the user's play record. This feature
is broken out into multiple exercises. Feel free to implement
some, all or, none (but why?!) of them.

Download https://goo.gl/Jk9ZCV file and put it in the same directory
as this Hangman Python file. The file contains two numbers separated
by a comma. The first number is the number of wins, and the second
number is the total number of plays (notice they're conveniently
defaulted to zero).

Write a function that reads from the newly downloaded file
and returns a 2-element list. The first element should be the number
of wins, and the second element should be the total number of plays.
'''
def GetPlayRecord():
    f = open('hangman_play_record.txt')
    for i in f:
        lst = i.strip().split(',')
    f.close()
    for j in range(len(lst)):
        lst[j] = int(lst[j])
    return lst


ans = GetPlayRecord()
# Don't worry about the isinstance function, the if statement, or what
# they do: it's not required for this Hangman assignment.
if ans != None and isinstance(ans[0], int) and isinstance(ans[1], int):
    text = 'PASS'
else:
    text = 'FAIL'
print('GetPlayRecord #1: expected int elements,', text)


'''-----------------------------------------------------------
Extra credit exercise 2:
Write a function that records whether the user played and won or
lost in the 'hangman_play_record.txt' file. The parameter should
be a boolean type, where True signifies a win and False signifies
a loss. Read Extra credit exercise 1 for information about the 
format of the 'hangman_play_record.txt' file.
'''
def RecordPlay(win):
    z = GetPlayRecord()
    write_win = open('hangman_play_record.txt', 'w')
    if win == 'True':
        z[0] += 1
    z[1] += 1
    z = str(z[0]) + ',' + str(z[1])
    write_win.write(z)
    write_win.close()


'''-----------------------------------------------------------
Extra credit exercise 3:
This function should be an expansion of StartupAndPlay. NOTE: even
if you do this bonus exercise, leave your StartupAndPlay function
as is!

First, copy all of the code you wrote for StartupAndPlay into this
new function. Add in the following:
* Code that makes use of GetPlayRecord and RecordPlay.
* When playing Hangman for the first time, display how many times
  the user win, and how many games they've played
* Each time the user wins or loses a single play of Hangman,
  display their new number of wins and total games played.
'''
def StartupAndPlayVersion2():
    c = GetPlayRecord()
    print('No. of wins: ', c[0])
    print('Total played: ', c[1])
    
    win = Play(GetRandomWord(words))
    print(win)

    if win == 'WOW, YOU WIN':
        RecordPlay('True')
    else:
        RecordPlay('False')

    ask = input('Do you want to play again?(y/n)')
    if ask == 'y':
        StartupAndPlayVersion2()
    print('No. of wins: ', GetPlayRecord()[0])
    print('Total played: ', GetPlayRecord()[1])


'''-----------------------------------------------------------
Extra credit exercise 4:
1. Copy the code you wrote for Exercise 6 and paste it here, but
   instead of calling StartupAndPlay, call StartupAndPlayVersion2.
   DO NOT change your answer for Exercise 6!
2. Comment out the code you wrote for Exercise 6. Again, DO NOT
   delete the code you wrote for Exercise 6!
'''
def main():
    StartupAndPlayVersion2()

    
if __name__ == "__main__":
    # execute only if run as a script
    main()
