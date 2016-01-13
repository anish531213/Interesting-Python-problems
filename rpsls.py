#Rock, paper, sissor, lizard, spock
#rock
#spock
#paper
#lizard
#sissors
import random


def rspls(user_input):
    user_input = user_input.lower()
    if user_input == "rock":
        user = 0
    elif user_input == "spock":
        user = 1
    elif user_input == "paper":
        user = 2
    elif user_input == "lizard":
        user = 3
    elif user_input == "sissors":
        user = 4
    mini(user)

def mini(x):
    y = random.randint(0, 4)
    z = x - y
    k = x - y
    if z == -1 or z == -2 or z == -3 or z == -4:
        k =  z % 5
    if k == 0:
        print("It's Draw")
    elif k == 1 or k == 2:
        print("You win!!!")
    else:
        print("you lose!!")
user_input = input(" Rock, spock, paper, lizard or sissors")
rspls(user_input)
    
        

