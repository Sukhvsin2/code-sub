class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            elif n > minHeap[0]:
                heapq.heapreplace(minHeap, n)

        
        return minHeap[0]