class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = 0
        zero_idx = -1
        for i, n in enumerate(nums):
            if n == 0: 
                zero_count+=1
                zero_idx = i
            if zero_count > 1: return [0] * len(nums)

        product = 1
        for n in nums:
            if n != 0:
                product *= n

        if zero_count:
            # do something
            answer = [0] * len(nums)
            answer[zero_idx] = product
        else:
            answer = []
            for n in nums:
                    answer.append(int(product / n))

        return answer
