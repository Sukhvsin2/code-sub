class Twitter:

    def __init__(self):
        # hashmap to store users
        self.followMap = defaultdict(set) # user: (followees, ...)
        self.tweetsMap = defaultdict(list) # user : [(time, tweetId), ...]
        self.time = 0 # time counter

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append([self.time, tweetId])
        self.time += 1 # current time, increment so can create a min heap

    def getNewsFeed(self, userId: int) -> List[int]:
        
        feed = deque()
        minHeap = []

        # add self to the followee
        self.followMap[userId].add(userId)

        # find all followers
        followees = self.followMap[userId]

        # traverse all followees and find all tweets
        for followeeId in followees:
            # all tweets from each followee into minHeap
            if followeeId in self.tweetsMap: # gives all tweets
                # add in minheap, if minHeap > 10 then pop the minheap
                for tweet in self.tweetsMap[followeeId]:
                    heapq.heappush(minHeap, tweet)

                    if len(minHeap) > 10:
                        heapq.heappop(minHeap)

        # at the end minHeap has all top 10 tweets
        # add into feed queue from left since we have min heap so older tweets are on top.
        while minHeap:
            feed.appendleft(heapq.heappop(minHeap)[1])

        return list(feed)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
