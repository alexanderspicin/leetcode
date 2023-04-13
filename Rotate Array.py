"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for pos in range(k):
            nums.insert(0, nums.pop())
