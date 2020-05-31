'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def solution(nums, k):
    '''
    nums: list of integers
    k: value to be reached by summing any two elements in nums
    '''

    # For O(N^2) do this:
    for i in nums:
        for j in nums:
            if i+j == k:
                return True
    return False

def solution_eff(nums, k):
    '''
    nums: list of integers
    k: value to be reached by summing any two elements in nums
    '''
   # To obtain O(N) complexity, we can do this:

    nums = set(nums)
    for i in nums:
        if k-i in nums: return True
    return False

print(solution([10,15,3,7],10))
print(solution_eff([10,15,3,7],10))
