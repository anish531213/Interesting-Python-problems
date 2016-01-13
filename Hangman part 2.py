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
pass


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
    pass


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
    pass


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
    pass


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
    pass


'''-----------------------------------------------------------
Exercise 6:
So far, whenever we've created a function inside of a script, we just
write a function call to use it. There's a more correct way to call
functions inside of a script.
* This page contains the code you'll need: https://goo.gl/9vebJU
* This page explains the code: http://goo.gl/JkGHX2
'''
pass


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
    pass


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
    pass


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
    pass


'''-----------------------------------------------------------
Extra credit exercise 4:
1. Copy the code you wrote for Exercise 6 and paste it here, but
   instead of calling StartupAndPlay, call StartupAndPlayVersion2.
   DO NOT change your answer for Exercise 6!
2. Comment out the code you wrote for Exercise 6. Again, DO NOT
   delete the code you wrote for Exercise 6!
'''
pass
