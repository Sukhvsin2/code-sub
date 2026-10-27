class Twitter:

    def __init__(self):
        # hashmap to store users
        self.followMap = defaultdict(set) # user: (followees, ...)
        self.tweetsMap = defaultdict(list) # user : [(time, tweetId), ...]
        self.time = 0 # time counter

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append([self.time, tweetId])
        self.time -= 1 # current time, decrement so can create a max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = [] # top 10 tweets
        minheap = []

        self.followMap[userId].add(userId)
        # get all tweets from followee people
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetsMap: # if a followee has at least 1 tweet
                index = len(self.tweetsMap[followeeId])-1
                time, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(minheap, [time, tweetId, followeeId, index - 1])

        while minheap and len(feed) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minheap)
            feed.append(tweetId)
            
            if index >= 0:
                time, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(minheap, [time, tweetId, followeeId, index-1])


        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
