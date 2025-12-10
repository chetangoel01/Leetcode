class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = curr = 0
        dic = {0: -1}

        # curr is the prefix sum up to the current int
        for i in range(len(nums)):
            num = nums[i]
            
            if num == 1:
                curr += 1
            else: curr -= 1

            if curr in dic:
                length = i - dic[curr]
                ans = max(ans, length)
            else: dic[curr] = i
                
        return ans