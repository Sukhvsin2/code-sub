class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # build the freq map
        counts = Counter(tasks)
        
        # build a max heap with freqs
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)
        
        # build a processing queue
        q = deque()
        time = 0

        # process it each freq and add next number to queue for next time to process
        while maxHeap or q:
            # count each time 
            time += 1

            # check if we have something in maxHeap
            if maxHeap:
                process_task = 1 + heapq.heappop(maxHeap)

                # if this task is not 0 then we have to process more
                if process_task:
                    # add in the queue to process it next with cool down time.
                    q.append([process_task, time + n]) # here n is the cool down time
                    # so we dont process it until time == time+n

            if q and q[0][1] == time: # process item from q since cool down time is done.
                heapq.heappush(maxHeap, q.popleft()[0])

        # return time
        return time