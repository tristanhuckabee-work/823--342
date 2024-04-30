"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
    for i, num in enumerate(nums):
        print(i)
        print(target - num)
        comp = nums[i + 1:].index(target - num)
        print(i, comp)
        if comp != -1 and comp != i:
            return [i, comp]

test_a = [[2, 7, 11, 15], 9]
test_b = [[3, 2, 4], 6]
test_c = [[3, 3], 6]

print(twoSum(*test_a)) # [0, 1]
print(twoSum(*test_b)) # [1, 2]
print(twoSum(*test_c)) # [0, 1]