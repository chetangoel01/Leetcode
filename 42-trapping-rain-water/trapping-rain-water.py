class Solution:
    def trap(self, height: List[int]) -> int:
        # it looks like for each bar im trying to find the next tallest bar (?)
        # almost trying to find subsequences with smaller numbers between them and 2 largest numbers on either side
        # i know this is a 2 pointer problem, what if we take a left and right pointer, move and just add the difference of the previous larger number - the smaller number. move the right pointer if current bar is higher than the one on the right?
        left = 0
        n = len(height)
        right = n - 1
        water = 0
        leftmax = height[left]
        rightmax = height[right]
        maxheight = min(leftmax, rightmax)

        while left < right:

            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            maxheight = min(leftmax, rightmax)
            
            if leftmax > rightmax:
                # move right
                water += maxheight - height[right]
                right -= 1
            else:
                water += maxheight - height[left]
                left += 1
    
        return water