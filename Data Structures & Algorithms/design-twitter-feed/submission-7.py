from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.tweet_idx = 0
        self.account_to_followees = {}
        self.account_to_tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.account_to_followees:
            self.account_to_followees[userId] = {userId}

        if userId not in self.account_to_tweets:
            self.account_to_tweets[userId] = []
        self.account_to_tweets[userId].append((-self.tweet_idx, tweetId))

        self.tweet_idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.account_to_followees:
            return []

        tweet_heap = []
        for followeeId in self.account_to_followees[userId]:
            if followeeId not in self.account_to_tweets:
                continue

            last_idx = len(self.account_to_tweets[followeeId]) - 1
            heapq.heappush(tweet_heap, (self.account_to_tweets[followeeId][last_idx], (followeeId, last_idx)))

        feed = []
        while tweet_heap and len(feed) < 10:
            newest_tweet = heapq.heappop(tweet_heap)

            tweet_id = newest_tweet[0][1]
            feed.append(tweet_id)

            followeeId, cur_followee_tweet_idx = newest_tweet[1]
            if cur_followee_tweet_idx == 0:
                continue
            next_tweet = self.account_to_tweets[followeeId][cur_followee_tweet_idx - 1]
            heapq.heappush(tweet_heap, (next_tweet, (followeeId, cur_followee_tweet_idx - 1)))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.account_to_followees:
            self.account_to_followees[followerId] = {followerId}
        self.account_to_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId == followeeId or followerId not in self.account_to_followees
            or followeeId not in self.account_to_followees[followerId]):
            return

        self.account_to_followees[followerId].remove(followeeId)