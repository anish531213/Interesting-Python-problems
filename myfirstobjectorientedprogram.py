import turtle

def make_line():

    wdow = turtle.Screen()
    anish = turtle.Turtle()
    wdow.bgcolor("red")
    anish.color("white")
    anish.speed(10)
    
    n = 24
    
    while n>0:
        i = 4
        for i in range(i, 0, -1):
            anish.forward(100)
            anish.right(90)
        anish.right(15)
        n -= 1
        


    kane = turtle.Turtle()
    kane.forward(100)
    kane.color("pink")
    kane.speed(10)
    

    k = 4
    while k>0:
        j = 90
        for j in range(j, 0, -1):
            kane.forward(5)
            kane.right(3)
        kane.right(180)
        k -= 1

        
        
make_line()

