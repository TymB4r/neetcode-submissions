from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.tweet_idx = 0
        self.account_to_feed = {}
        self.account_to_tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.account_to_feed:
            self.account_to_feed[userId] = {userId}

        if userId not in self.account_to_tweets:
            self.account_to_tweets[userId] = []
        self.account_to_tweets[userId].append((-self.tweet_idx, tweetId)) # -self.tweet_idx to maintain a max_heap

        self.tweet_idx += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_heap = []
        for vendorId in self.account_to_feed[userId]:
            if vendorId not in self.account_to_tweets:
                continue
            account_size = len(self.account_to_tweets[vendorId])
            heapq.heappush(tweet_heap, (self.account_to_tweets[vendorId][account_size - 1], (vendorId, account_size - 1)))

        feed = []
        while tweet_heap and len(feed) < 10:
            newest_tweet = heapq.heappop(tweet_heap)
            vendor, vendors_tweet = newest_tweet[1]
            feed.append(self.account_to_tweets[vendor][vendors_tweet][1])
            vendor, vendors_tweet = newest_tweet[1]
            if vendors_tweet == 0:
                continue

            heapq.heappush(tweet_heap, (self.account_to_tweets[vendor][vendors_tweet - 1], (vendor, vendors_tweet - 1)))

        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.account_to_feed:
            self.account_to_feed[followerId] = {followerId}
        self.account_to_feed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId == followeeId or followerId not in self.account_to_feed
            or followeeId not in self.account_to_feed[followerId]):
            return

        self.account_to_feed[followerId].remove(followeeId)