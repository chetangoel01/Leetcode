class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq = Counter(nums)
        heap = []
        for n, freq in numfreq.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]