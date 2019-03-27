import turtle

myTurtle = turtle.Turtle() # initiate a turtle object
myWin = turtle.Screen() # show the turtle on the screen

def drawSpiral(myTurtle, lineLen):
    """draw a rectangular spiral
    myTurtle: turtle
    lineLen: length of one movement"""
    
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()