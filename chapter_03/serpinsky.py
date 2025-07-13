import turtle as t

def triangle(t, size):

    if size > 1: # this avoids recursion when size is 1

        t.forward(size)
        triangle(t, size/2) # this is the recursive call
        t.right(120)
        t.forward(size)
        triangle(t, size/2) # this is the recursive call
        t.right(120)
        t.forward(size)
        triangle(t, size/2) # this is the recursive call
        t.right(120)

nellie = t.Turtle()
nellie.hideturtle()
nellie.speed("fastest")
nellie.penup()
nellie.goto(-200,150) # move the starting point
nellie.pendown()

triangle(nellie, 256)

t.mainloop()
