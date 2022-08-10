from typing import List

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        el_index = 0
        exception_values = []
        for el in numbers:
            el_index += 1
            if el in exception_values:
                continue
            need_found = target - el
            try:
                found_index = numbers.index(need_found)
                if el_index - 1 != found_index:
                    return sorted([el_index , found_index + 1])
                else:
                    continue
            except ValueError:
                exception_values.append(el)
                continue