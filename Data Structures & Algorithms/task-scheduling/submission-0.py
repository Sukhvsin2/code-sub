class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a hash map with freq
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()] # count.values() only values of the map
        heapq.heapify(maxHeap) # Max Heap

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1 # count time every iteration
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt: # if cnt is not zero means we have tasks left.
                    # so we add same task into q to process but after current + cooldown
                    q.append([cnt, time + n]) # here n is the cooldown time.

            if q and q[0][1] == time: # item in q's cooldown time is done.
                # process from left since FIFO
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
