"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution(object):
    def rotate(self, nums, k):
        nums_2 = nums.copy()
        nums.clear()
        a = k % len(nums_2)
        nums.extend(nums_2[-a:])
        nums.extend(nums_2[:-a])
