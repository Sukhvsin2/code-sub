class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x > y:
                heapq.heappush(maxHeap, -(x - y))
            else:
                heapq.heappush(maxHeap, -(y - x))
        
        if not len(maxHeap): return 0

        return -maxHeap[0]