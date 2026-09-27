"""
thoughts:
order matters --> handled by deque
limit on feed posts --> in specific function not in init 

user: following --> hashmap
posts deque, with all the necessary details 


"""
from collections import deque, defaultdict
class Twitter:

    def __init__(self):
        self.posts = deque()
        self.follow_pairs = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #append to the posts deque
        self.posts.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        fetches at most the 10 most recent
        """
        feed = []
        for posterid, tweetid in self.posts:
            if posterid == userId or posterid in self.follow_pairs[userId]:
                feed.append(tweetid)
                if len(feed) >= 10:
                    break
        return feed
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        user can't follow themself
        """
        if followerId != followeeId:            
            self.follow_pairs[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_pairs[followerId].discard(followeeId)
        
