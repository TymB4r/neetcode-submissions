from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        self.parent[y] = self.find(x)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uf = UnionFind()

        for num in nums:
            uf.parent[num] = num

        for num in nums:
            if num - 1 in nums:
                uf.union(num - 1, num)
            if num + 1 in nums:
                uf.union(num, num + 1)

        parent_to_count = {}
        for parent in uf.parent.values():
            if parent not in parent_to_count:
                parent_to_count[parent] = 1
            else:
                parent_to_count[parent] += 1

        return max(parent_to_count.values())