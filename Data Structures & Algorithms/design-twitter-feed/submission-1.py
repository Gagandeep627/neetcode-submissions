from heapq import heappush, heappop
from collections import defaultdict

class Twitter:

    # topic : Heapq // Priority queue-->

    def __init__(self):
        # set time : 0, tweet : dict(list), follows(set) -->
        self.time = 0
        # Space = O(N * M)
        self.tweet = defaultdict(list)
        # Space = O(N * F)
        self.follows = defaultdict(set)
    #Time = O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        # exceed time by one for that userId
        # the add (time, tweet id) --> to the tweet dictionary..
        # a person will follow himself on the self.follows--> 
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))
        self.follows[userId].add(userId)

        # return

    def getNewsFeed(self, userId: int) -> List[int]:

        # space O(F)
        max_heap = []
        # Heap push for each → F pushes
        # for each follower for --> userId
        for followee in self.follows[userId]:
            # check for the tweet --> userId:
            if (self.tweet[followee]):
                # for time, tweet_id : (self.tweet[followee][-1]). : ??
                time, tweet_id = self.tweet[followee][-1]

                index = len(self.tweet[followee]) - 1 #calculate index : for the tweets(follower) -->
                # Each push → O(log F)
                heappush(max_heap, (-time, tweet_id, followee, index)) #add to the heappush((max_heap, (-time, tweet_id, followee, index))) -->

        # So Step A = O(F log F)
        result = [] #make a result array-->

        while max_heap and len(result) < 10: # untill max_heap && len(result) < 10:
            # Each pop = O(log F)
            time, tid, uid, idx = heappop(max_heap) #take top from the heap -->(time, tweet_id, follow_id, index) -->

            result.append(tid) #add(tweet id to --> result);

            if (idx > 0): # (if (idx > 0):)
                next_time, next_tid = self.tweet[uid][idx-1] # next_time, next_tid = tweet[foillow_id][prev_index] (a)
                # O(log F)
                heappush(max_heap, (-next_time, next_tid, uid, idx-1)) # addlto the heap (A) ++ (follow_id, prev_index)

        # time : 👉 O(F log F)
        return result #return : result;

        
    # Time = O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId) # each person follow himself-->
        
# Time = O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # regardless unfollowing itself from the follows dict --> remove the 
        # except that follows (removing himself from the self.follows) -->
        # remoce each and every one from the (self.follows)-->
        if ((followerId) != (followeeId)):
            self.follows[followerId].discard(followeeId) 



    # space complexity : 👉 O(NM + NF + F), O(NM + NF)

# Heap space is small in comparison.
    # return result