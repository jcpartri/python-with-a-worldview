# collections is part of the Python standard library.
# it has been around for a very long time.
from collections import deque 
 
# Create a Stack class that inherits from deque
class Stack(deque): 
    def __init__(self): 
        super().__init__() 
 
    # we do need to create our own push() method. 
    # if we do not, then we have to use append(). 
    def push(self, e): 
        self.append(e) 
 
    # there is already a pop() method, so we 
    # do not have to implement that one. 
 
# Create our stack instance 
stack = Stack() 
 
# Push some elements onto the stack. 
stack.push("a") 
stack.push("b") 
stack.push("c") 
print(stack) 
# Output: Stack(['a', 'b', 'c']) 
 
# Remove an element from the stack. 
e = stack.pop()
print(f"The item popped off the stack was: {e}")
print(f"The items remaining on the stack are: {stack}") 
# Output: Stack(['a', 'b'])
