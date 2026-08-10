from collections import defaultdict
import heapq

class Twitter:
    # solution1 exceeded time limit: loop took o(n) time 
    # invriants: number of posts/accounts never decreases
    def __init__(self):
        self.count = 0 # oldest tweet = 0, more negative = more recent
        self.users = defaultdict(set) # key: user, val: users_following
        self.posts = defaultdict(list) # key: user, val: [posts from user, recency]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1  # decrement for tracking recency
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.users[userId].add(userId)

        for followee in self.users[userId]:
            if followee in self.posts: # has atleast one post 
                index = len(self.posts[followee]) - 1 # gather posts of followers
                count, tweetID = self.posts[followee][index] 
                minHeap.append([count, tweetID, followee, index-1]) # append curr recency/id, followee/index-1 for next post by followee
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            # retrieve heap top (most recent)
            recency, tweetID, followee, index = heapq.heappop(minHeap)
            res.append(tweetID)

            if index >= 0:
                # add next post by followee to heap
                recency, tweetID = self.posts[followee][index]
                heapq.heappush(minHeap, [recency, tweetID, followee, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)