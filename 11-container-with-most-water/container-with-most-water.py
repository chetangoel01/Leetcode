class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        left = 0
        right = n-1
        max_volume = -inf
        while right > left:
            left_height = height[left]
            right_height = height[right]
            max_volume = max((right - left) * min(left_height, right_height), max_volume)
            
            if left_height < right_height:
                left = left + 1
            else:
                right = right - 1

        return max_volume