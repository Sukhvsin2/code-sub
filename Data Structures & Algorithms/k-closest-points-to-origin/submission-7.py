class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # save all distances
        # q: Struct to save the Heap Vals
        '''
        val : (distance, index?)
        '''
        # create a minheap 
        minHeap = []
        for index, point in enumerate(points):
            heapq.heappush(minHeap, (math.sqrt((point[0]-0)**2 + (point[1]-0)**2), index))

        res = []
        while k:
            k-=1
            res.append(points[heapq.heappop(minHeap)[1]])
        # get the index values in a res
        # will return K minimum vals from the minheap tree
        return res
