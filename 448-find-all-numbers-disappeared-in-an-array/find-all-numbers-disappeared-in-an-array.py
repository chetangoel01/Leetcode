class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsset = set(nums)
        arr = []
        for i in range(1, len(nums)+1):
            if i not in numsset:
                arr.append(i)
        return arr