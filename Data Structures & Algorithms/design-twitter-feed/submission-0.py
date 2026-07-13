class Twitter:

    def __init__(self):
        self.fmap = defaultdict(set)
        self.tmap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.fmap[userId].add(userId)
        for f in self.fmap[userId]:
            if f in self.tmap:
                index = len(self.tmap[f]) - 1
                count, tweetId = self.tmap[f][index]
                minheap.append([count, tweetId, f, index - 1])
        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count, tweetId, f, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tmap[f][index]
                heapq.heappush(minheap, [count, tweetId, f, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fmap[followerId]:
            self.fmap[followerId].remove(followeeId)
