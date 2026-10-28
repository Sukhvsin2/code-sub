import heapq

class MedianFinder:
    def __init__(self):
        self.left = [] # maxHeap
        self.right = [] # minHeap

    def addNum(self, num: int) -> None:
        if self.left and -num < self.left[0]: # if left is not empty and num is bigger 
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num) # -num to create maxHeap

        # rebalance both heaps
        if len(self.left) + 1 < len(self.right):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val) # since pushing into maxHeap
        elif len(self.right) + 1 < len(self.left):
            val = -heapq.heappop(self.left) # since popping from maxHeap
            heapq.heappush(self.right, val)
        # else they both are equal so do nothing.

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2.0
        else:
            return self.right[0] if len(self.left) < len(self.right) else -self.left[0]
        