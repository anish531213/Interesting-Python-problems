import turtle

def make_line():

    wdow = turtle.Screen()
    anish = turtle.Turtle()
    wdow.bgcolor("red")
    
    n = 5
    
    while n>0:
        i = 4
        for i in range(i, 0, -1):
            anish.forward(100)
            anish.right(90)
        anish.right(15)
        
        
make_line()

