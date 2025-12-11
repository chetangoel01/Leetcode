from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mon_dec_queue = deque()
        ans = []

        for i, num in enumerate(nums):
            # 1. Remove indices that fall out of the window
            while mon_dec_queue and mon_dec_queue[0] <= i - k:
                mon_dec_queue.popleft()

            # 2. Maintain decreasing order
            while mon_dec_queue and nums[mon_dec_queue[-1]] < num:
                mon_dec_queue.pop()

            # 3. Add current index
            mon_dec_queue.append(i)

            # 4. Start recording results once first window is full
            if i >= k - 1:
                ans.append(nums[mon_dec_queue[0]])

        return ans