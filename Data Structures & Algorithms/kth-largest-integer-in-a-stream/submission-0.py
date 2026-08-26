from sortedcontainers import SortedList
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.search_tree = SortedList(nums)

    def add(self, val: int) -> int:
        self.search_tree.add(val)
        return self.search_tree[len(self.search_tree) - self.k]