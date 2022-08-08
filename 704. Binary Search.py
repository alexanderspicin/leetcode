class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)
        while low <= high:
            middle = int((low + high) / 2)
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                high = middle
            else:
                low = middle


