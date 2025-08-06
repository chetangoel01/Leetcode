import numpy as np

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        slice_counter = 0
        result = 0
        if len(nums) < 3:
            return 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                slice_counter += 1
                result += slice_counter
            else:
                slice_counter = 0
        return result