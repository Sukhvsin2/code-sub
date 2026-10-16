class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # base case
        if len(stones) == 1:
            return stones[0]

        # maintain a max heap
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        # compare largest 2 values until len of stones is 1
        while len(maxHeap) > 1:
            # poped 2 max elements
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x > y:
                heapq.heappush(maxHeap, -(x-y))
            elif y > x:
                heapq.heappush(maxHeap, -(y-x))

        if not len(maxHeap): return 0

        return -maxHeap[0]