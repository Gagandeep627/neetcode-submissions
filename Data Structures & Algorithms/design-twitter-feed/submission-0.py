from heapq import heappush, heappop
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))
        self.follows[userId].add(userId)

        # return

    def getNewsFeed(self, userId: int) -> List[int]:


        max_heap = []

        for followee in self.follows[userId]:

            if (self.tweet[followee]):
                time, tweet_id = self.tweet[followee][-1]

                index = len(self.tweet[followee]) - 1

                heappush(max_heap, (-time, tweet_id, followee, index))

        
        result = []

        while max_heap and len(result) < 10:
            time, tid, uid, idx = heappop(max_heap)

            result.append(tid)

            if (idx > 0):
                next_time, next_tid = self.tweet[uid][idx-1]
                heappush(max_heap, (-next_time, next_tid, uid, idx-1))


        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
 
        if ((followerId) != (followeeId)):
            self.follows[followerId].discard(followeeId)



        
    # return result