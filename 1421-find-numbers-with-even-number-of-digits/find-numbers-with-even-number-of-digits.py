class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def isEvenDigits(num):
            numDigits = len(str(num)) % 2
            return numDigits == 0
        
        count = 0
        for num in nums:
            if isEvenDigits(num): count+=1
        
        return count