'''
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

There are two bonuses this week.

Bonus 1

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️

>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
Bonus 2

For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️

>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
'''

def add(m1,m2):
    # Assuming matrices have same shapes
    m = []
    for row1,row2 in zip(m1,m2):
        row = []
        for col1,col2 in zip(row1,row2):
            row.append(col1+col2)
        m.append(row)
    return m

def add_argv(*arg):
    if len(arg) == 1:
        return arg[0]

    add_argv(arg[1:])
matrix1 = [[1, -2], [-3, 4]]
matrix3 = [[1, -2], [-3]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1,matrix2))
print(add_argv(matrix1,matrix2))
