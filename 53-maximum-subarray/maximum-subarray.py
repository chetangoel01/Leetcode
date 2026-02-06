class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # this is a prefix sum problem for sure
        prefixsum = [nums[0]]
        for i in range(1, len(nums)):
            prefixsum.append(prefixsum[-1] + nums[i])

        max_sum = -inf
        min_bf = 0
        for i in range(len(prefixsum)):
            max_sum = max(max_sum, prefixsum[i] - min_bf)
            min_bf = min(min_bf, prefixsum[i])

        return max_sum