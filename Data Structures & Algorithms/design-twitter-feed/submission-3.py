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
        for followeeId in self.account_to_feed[userId]:
            if followeeId not in self.account_to_tweets:
                continue

            last_idx = len(self.account_to_tweets[followeeId]) - 1
            heapq.heappush(tweet_heap, (self.account_to_tweets[followeeId][last_idx], (followeeId, last_idx)))

        feed = []
        while tweet_heap and len(feed) < 10:
            newest_tweet = heapq.heappop(tweet_heap)

            tweet_id = newest_tweet[0][1]
            feed.append(tweet_id)

            vendor, cur_vendors_tweet_idx = newest_tweet[1]
            if cur_vendors_tweet_idx == 0:
                continue

            heapq.heappush(tweet_heap, (self.account_to_tweets[vendor][cur_vendors_tweet_idx - 1], (vendor, cur_vendors_tweet_idx - 1)))

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