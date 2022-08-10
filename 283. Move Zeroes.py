from typing import List

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums_copy = nums.copy()
        zero_list = []
        try:
            while True:
                index = nums_copy.index(0)
                zero_list.append(0)
                nums_copy.pop(index)
        except ValueError:
            nums.clear()
            nums.extend(nums_copy)
            nums.extend(zero_list)