"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def searchInsert(self, nums, target):
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
        return low
