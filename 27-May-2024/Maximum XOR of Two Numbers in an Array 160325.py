# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self) -> None:
        self.children = [None, None]
        self.is_end = False

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def insert(num):
            cur = trie
            for i in range(31, -1, -1):
                val = (num >> i) & 1
                if not cur.children[val]:
                    cur.children[val] = TrieNode()
                cur = cur.children[val]

        n = len(nums)
        trie = TrieNode()
        for num in nums:
            insert(num)

        rst = 0
        for num in nums:
            cur = trie
            max_xor = 0
            for i in range(31, -1, -1):
                val = not ((num >> i) & 1)
                if cur.children[val]:
                    max_xor += 2**i
                    cur = cur.children[val]
                else:
                    cur = cur.children[not val]
            rst = max(rst, max_xor)
        return rst
