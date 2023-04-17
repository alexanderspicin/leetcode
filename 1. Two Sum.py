from typing import List

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for position in range(len(nums)):
            nums_pop = nums.pop(position)
            if target - nums_pop in nums:
                if target - nums_pop == nums_pop:
                    return [position, nums.index(target - nums_pop) + 1]
                nums.insert(position, nums_pop)
                return [position, nums.index(target - nums_pop)]
            else:
                nums.insert(position, nums_pop)
