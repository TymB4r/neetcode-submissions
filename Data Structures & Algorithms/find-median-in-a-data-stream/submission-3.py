import heapq


class MedianFinder:

    def __init__(self):
        # left_half: max heap, right_half: min heap
        self.left_half = []
        self.right_half = []

    def addNum(self, num: int) -> None:
        if not self.right_half or num < self.right_half[0]: # If not right_half, default right_half[0] to infinity
            heapq.heappush(self.left_half, -num)
        else:
            heapq.heappush(self.right_half, num)

        if len(self.left_half) - len(self.right_half) > 1:
            heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        if len(self.right_half) - len(self.left_half) > 1:
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))


    def findMedian(self) -> float:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2

        if len(self.left_half) > len(self.right_half):
            return -self.left_half[0]
        return self.right_half[0]