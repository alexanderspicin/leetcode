"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = int((low + high) / 2)
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        return -1
