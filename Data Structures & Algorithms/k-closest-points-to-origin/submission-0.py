class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def cal(point):
            x, y = point[0], point[1]

            return math.sqrt((x-0)**2 + (y-0)**2)
        
        # save all distances
        # q: Struct to save the Heap Vals
        '''
        val : (distance, index?)
        '''
        # create a minheap 
        minHeap = []
        for index, point in enumerate(points):
            distance = cal(point)
            heapq.heappush(minHeap, (distance, index))
            # print(minHeap)

        res = []
        while k:
            k-=1
            res.append(points[heapq.heappop(minHeap)[1]])
        # get the index values in a res
        # will return K minimum vals from the minheap tree
        return res
