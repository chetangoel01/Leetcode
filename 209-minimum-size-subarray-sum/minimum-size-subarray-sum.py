class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        result = math.inf
        running_sum = 0
        while j < n:
            running_sum += nums[j]
            while running_sum >= target:
                result = min(result, j-i+1)
                running_sum -= nums[i]
                i += 1

            j += 1

        if result == math.inf:
            return 0
        return result