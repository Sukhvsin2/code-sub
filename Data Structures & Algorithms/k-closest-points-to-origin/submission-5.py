class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # build a K len of maxHeap
        maxHeap = []

        for i, p in enumerate(points):
            dis = (p[0] - 0)**2 + (p[1] - 0)**2
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dis, i))
            elif -dis > maxHeap[0][0]:
                heapq.heapreplace(maxHeap, (-dis, i))
        res = []
        for _, i in maxHeap:
            res.append(points[i])

        return res