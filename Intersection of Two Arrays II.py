from typing import List

"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
 Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection =[]
        for element in nums1:
            try:
                intersection.append(nums2.pop(nums2.index(element)))
            except ValueError:
                continue
        return intersection