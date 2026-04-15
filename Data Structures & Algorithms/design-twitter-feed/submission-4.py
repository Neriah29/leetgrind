"""
post tweets
follow user
unfollow user
view <= 10 recent tweets of those they follow

Thoughts:
alltweets = array [(tweetid, userid )]
for each user, append to the users map and map each user to their following

"""

class Twitter:

    def __init__(self):
        self.alltweets = deque([])
        self.users = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        append to the alltweets with the user id
        """
        self.alltweets.appendleft((tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        trying to return an array of:
        max len of 10
        from left to right order
        if userid == curruserid or if userid in self.users[userid]
        """
        news = []
        for tweet in self.alltweets:
            if len(news) >= 10:
                break
            if tweet[1] in self.users[userId] or tweet[1] == userId:
                news.append(tweet[0])
        
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        add the followeeid to the userid set in the map
        """
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
        
