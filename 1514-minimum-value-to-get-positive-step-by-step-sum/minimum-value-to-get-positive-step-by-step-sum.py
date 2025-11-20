class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        minSum = prefix[0]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
            minSum = min(minSum, prefix[-1])
            
        # [-3, 2, -3, 4, 2]
        # [-3, -1, -4, 0, 2]

        # x + minSum >= 1
        # x >= 1 - minSum

        return 1 - minSum if minSum < 1 else 1
