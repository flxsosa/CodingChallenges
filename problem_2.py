'''
Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
'''

def solution(arr):
    # O(n^2)
    # Without division
    product_list = []
    for item_1 in arr:
        accumulator = 1
        for item_2 in arr:
            if item_2 != item_1: accumulator*=item_2
        product_list.append(accumulator)
    return product_list

def solution_div(arr):
    # O(2n)
    # With division
    # Create array product
    product = 1
    for item in arr:
        product *= item
    return [product/item for item in arr]

arg = list(range(1,6))
print(solution(arg))
print(solution_div(arg))
