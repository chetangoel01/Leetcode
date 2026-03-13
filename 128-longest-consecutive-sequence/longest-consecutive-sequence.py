class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        numsset = set(nums)
        maxlength = -inf
        longest = -inf
        processed = {}

        for n in numsset:
            length = 1
            nextnum = n+1
            if n-1 in numsset:
                continue
            while nextnum in numsset:
                if nextnum in processed:
                    length += processed[nextnum]
                    break
                length += 1
                nextnum += 1
            
            if length > maxlength:
                maxlength = length
                longest = n
            
            processed[n] = length
        
        return maxlength