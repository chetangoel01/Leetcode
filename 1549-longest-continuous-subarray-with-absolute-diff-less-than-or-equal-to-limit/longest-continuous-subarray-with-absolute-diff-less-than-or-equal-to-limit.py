from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # one queue to keep track of window max
        # one queue to keep track of window min
        inc_queue = deque() # min
        dec_queue = deque() # max
        left = 0
        ans = 0
        # when maxdiff > limit, remove leftmost index and check whether in max/min and update maxdiff
        for right, n in enumerate(nums):
            # update ans when maxdiff updates within range
            while dec_queue and dec_queue[-1] < n:
                dec_queue.pop()
            dec_queue.append(n)

            # update min
            while inc_queue and inc_queue[-1] > n:
                inc_queue.pop()
            inc_queue.append(n)

            # shrink while invalid
            while dec_queue[0] - inc_queue[0] > limit:
                if nums[left] == dec_queue[0]:
                    dec_queue.popleft()
                if nums[left] == inc_queue[0]:
                    inc_queue.popleft()
                left += 1

            # valid window
            ans = max(ans, right - left + 1)

        return ans