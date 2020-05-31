'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    def extract(a,b):
        return a
    return pair(extract)

def cdr(pair):
    def extract(a,b):
        return b
    return pair(extract)

# With lambda expressions (cuz functional programming, yo)
def car_lambda(pair):
    return pair(lambda a,b: a)

def cdr_lambda(pair):
    return pair(lambda a,b: b)

print(car(cdr(cons("a",cons("b","c")))))
print(car_lambda(cdr_lambda(cons("a",cons("b","c")))))
