# Chapter 2 Quiz A with Solutions

This quiz contains 25 multiple choice questions for beginner to intermediate Python students, covering comparison operators, conditional statements, logical operators, lists, sets, list slicing, loops, range(), infinite loops, binary numbers, ASCII, data units, program scaffolding, specification sheets, and problem-solving. Each question has four answer choices. Select the correct option.

## Question 1
Which comparison operator checks if two values are not equal?

A) `==`  
B) `!=`  
C) `<>`  
D) `>=`

**Answer**: B) `!=`

## Question 2
What is the output of this code?

```python
x = 5
y = 10
if x <= y:
    print("Less or equal")
else:
    print("Greater")
```

A) Less or equal  
B) Greater  
C) Error  
D) Nothing

**Answer**: A) Less or equal

## Question 3
Which logical operator returns `True` if both operands are `True`?

A) `or`  
B) `and`  
C) `xor`  
D) `not`

**Answer**: B) `and`

## Question 4
What is the result of this expression?

```python
x = True
y = False
print(x or y)
```

A) True  
B) False  
C) Error  
D) None

**Answer**: A) True

## Question 5
How do you create an empty list in Python?

A) `my_list = {}`  
B) `my_list = []`  
C) `my_list = ()`  
D) `my_list = set()`

**Answer**: B) `[]`

## Question 6
What does this code do?

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
```

A) {1, 2, 3}  
B) {1, 2, 3, 4}  
C) [1, 2, 3, 4]  
D) Error

**Answer**: B) {1, 2, 3, 4}

## Question 7
What is the output of this list slicing?

```python
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])
```

A) [10, 20, 30]  
B) [20, 30, 40]  
C) [30, 40, 50]  
D) [10, 20, 30, 40]

**Answer**: B) [20, 30, 40]

## Question 8
What will this for loop print?

```python
for i in range(2, 5):
    print(i, end=" ")
```

A) 2 3 4  
B) 2 3 4 5  
C) 1 2 3 4  
D) 3 4 5

**Answer**: A) 2 3 4

## Question 9
Which of the following creates an infinite loop?

A) 
```python
while True:
    print("Loop")
```

B) 
```python
for i in range(5):
    print(i)
```

C) 
```python
x = 1
while x < 5:
    x += 1
```

D) 
```python
for i in range(1, 5, 2):
    print(i)
```

**Answer**: A)

## Question 10
What is the binary representation of the decimal number 13?

A) 1101  
B) 1011  
C) 1110  
D) 1001

**Answer**: A) 1101

## Question 11
What is the decimal equivalent of the binary number 1010?

A) 8  
B) 10  
C) 12  
D) 14

**Answer**: B) 10

## Question 12
What is the ASCII value of the character 'A'?

A) 65  
B) 97  
C) 48  
D) 32

**Answer**: A) 65

## Question 13
How many bits are in a byte?

A) 4  
B) 8  
C) 16  
D) 32

**Answer**: B) 8

## Question 14
How many bytes are in a kilobyte?

A) 100  
B) 1000  
C) 1024  
D) 1048

**Answer**: C) 1024

## Question 15
What will this code print?

```python
x = False
print(not x)
```

A) True  
B) False  
C) Error  
D) None

**Answer**: A) True

## Question 16
Which method removes a specific element from a set?

A) `pop()`  
B) `remove()`  
C) `delete()`  
D) `clear()`

**Answer**: B) `remove()`

## Question 17
What is the output of this code?

```python
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)
```

A) [1, 4, 2, 3]  
B) [4, 1, 2, 3]  
C) [1, 2, 4, 3]  
D) [1, 2, 3, 4]

**Answer**: A) [1, 4, 2, 3]

## Question 18
What does this while loop print?

```python
x = 0
while x < 3:
    print(x)
    x += 1
```

A) 0 1 2  
B) 1 2 3  
C) 0 1 2 3  
D) 0 1

**Answer**: A) 0 1 2

## Question 19
What is the result of this code?

```python
x = 7
y = 3
print(x > y and x != y)
```

A) True  
B) False  
C) Error  
D) None

**Answer**: A) True

## Question 20
Which of the following converts a decimal number to binary in Python?

A) `bin()`  
B) `int()`  
C) `hex()`  
D) `oct()`

**Answer**: A) `bin()`

## Question 21
What is the output of this code?

```python
my_list = ['a', 'b', 'c', 'd']
print(my_list[::2])
```

A) ['a', 'b']  
B) ['a', 'c']  
C) ['b', 'd']  
D) ['c', 'd']

**Answer**: B) ['a', 'c']

## Question 22
What is a key purpose of scaffolding a program?

A) Writing the final code  
B) Creating a basic structure to guide development  
C) Testing the program  
D) Deploying the program

**Answer**: B) Creating a basic structure to guide development

## Question 23
What should a specification sheet for a program include?

A) Only the final code  
B) Program requirements, inputs, outputs, and constraints  
C) Only the user interface design  
D) Only the testing results

**Answer**: B) Program requirements, inputs, outputs, and constraints

## Question 24
What will this code print?

```python
x = 0b1100
print(int(x))
```

A) 12  
B) 1100  
C) 6  
D) 8

**Answer**: A) 12

## Question 25
Which approach is most effective for problem-solving using code?

A) Writing code without planning  
B) Breaking the problem into smaller, manageable parts  
C) Using only built-in functions  
D) Copying code from the internet

**Answer**: B) Breaking the problem into smaller, manageable parts
