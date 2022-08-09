"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
import random
from math import pow

class Solution(object):
    def sortedSquares(self, nums):
        squares_num = [x * x for x in nums]
        return self.quick_sort(squares_num)

    def quick_sort(self, digits):
        if len(digits) <= 1:
            return digits
        else:
            q = random.choice(digits)
            s_nums = []
            m_nums = []
            e_nums = []
            for dig in digits:
                if dig < q:
                    s_nums.append(dig)
                elif dig > q:
                    m_nums.append(dig)
                else:
                    e_nums.append(dig)
            return self.quick_sort(s_nums) + e_nums + self.quick_sort(m_nums)


