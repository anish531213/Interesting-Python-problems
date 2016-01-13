'''-----------------------------------------------------------
CS 100 Homework #2. Upload completed files to Blackboard by Friday, Oct 23rd at 11:59PM.

1. Everything in this entire file must be valid Python!
2. Do not change any pre-existing function names, but feel free to create new functions with their own unique names.
3. Implement your solutions by removing the pass keyword and writing your answer.
4. Sample function calls are provided, but your functions will be tested against a variety of values.
5. In order to submit on Blackboard, you'll probably need to paste all content in this Doc into a .py file (Python file) and submit that.
6. For more info on the pass keyword: http://goo.gl/rnA20w

Grading:
1. Each question has equal worth.
2. This homework is out of 110 points: 10 of those points count towards extra credit.
3. Both the validity and styling of your solutions will be graded.
'''


'''-----------------------------------------------------------
SAMPLE exercise:
Write a function that takes an integer and returns True if the integer is even and false otherwise.
'''
def IsEven(x):
    return x % 2 == 0


answer = IsEven(231)
print('IsEven: expected False, got', answer)


'''-----------------------------------------------------------
Exercise 1:
Using recursion (no loops), write a function that returns the sum of all digits within an integer. Do not cast the integer to a string!
'''
def GetDigitSumRecursion(number):
    if number < 10:
        return number
    else:
        return (number%10) + GetDigitSumRecursion(number//10)
answer = GetDigitSumRecursion(217074)
print('GetDigitSumRecursion #1: expected 21, got', answer)
answer = GetDigitSumRecursion(90210)
print('GetDigitSumRecursion #2: expected 12, got', answer)


'''-----------------------------------------------------------
Exercise 2:
Reimplement Exercise 1 using a while loop (no recursion). Do not cast the integer to a string!
'''
def GetDigitSumLoop(number):
    z = 0
    while number!=0:
        x = number % 10
        z += x
        n = number // 10
    return(z)

answer = GetDigitSumLoop(7770777)
print('GetDigitSumLoop: expected 6, got', answer)


'''-----------------------------------------------------------
Exercise 3:
Using a while loop, write a function that reverses a string. (If you know about the string slicing technique "word"[::-1], do not use it.)
'''
def GetReverse(word):
    n = len(word) - 1
    z = ''
    while n >= 0:
        z += word[n]
        n -= 1
    return z

answer = GetReverse('banana')
print('GetReverse: expected "ananab", got', answer)


'''-----------------------------------------------------------
Exercise 4:
Using either a while loop or recursion, write a function that returns True if the number is prime and False otherwise. Hint: A prime number is greater than 1 and can be divided evenly only by 1 or itself.
'''
def IsPrime(n):
    m = 1
    i = 0
    while m<=n:
        if n%m == 0:
            i += 1
        m += 1
    if i == 2:
        return True
    else:
        return False

answer = IsPrime(11)
print('IsPrime: expected True, got', answer)


'''-----------------------------------------------------------
Exercise 5:
Write a function that returns a string with the first and last characters removed. The string parameter's length will be at least 2. Hint: you'll need to read about Python string slicing here: https://goo.gl/P7ju2L
'''
def GetInside(word):
    new_word = word[1:(len(word)-1)]
    return new_word

answer = GetInside('trips')
print('GetInside #1: expected "rip", got', answer)
answer = GetInside('so')
print('GetInside #2: expected an empty string, got', answer)


'''-----------------------------------------------------------
Exercise 6:
A perfect number is a number whose factors (excluding itself) sum to that number. For example, 6 is a perfect number because its factors 1, 2, and 3 sum to 6. Also, the factors of 28 are 1+2+4+7+14=28. Write a function (while loop or recursion) that returns True if the number is perfect and false otherwise. 
'''
def IsPerfect(n):
    i = 1
    m = 0
    while i < n:
        if n%i == 0 :
            m += i
        i += 1
    if m == n:
        return True
    else:
        return False

answer = IsPerfect(496)
print('IsPerfect: expected True, got', answer)
