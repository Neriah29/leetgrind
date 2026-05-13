class Twitter:

    def __init__(self):
        self.fol = defaultdict(set)
        self.tweets = deque([])


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((tweetId,userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for tw_id, us_id in self.tweets:
            if len(feed) >= 10:
                break
            if us_id in self.fol[userId] or us_id == userId:
                feed.append(tw_id)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].remove(followeeId)
        
