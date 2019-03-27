""" draw a fractal tree, a visualizing recursion¶"""

import turtle

def tree(branchLen,t):
    """The branches are from right to left and then go back to the origin"""
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)  
    t.up() # do not show the trace
    t.backward(100)
    t.down() # do not show the trace
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()