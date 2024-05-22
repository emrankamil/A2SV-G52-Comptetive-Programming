# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hmap = defaultdict(int)
        longest = 1
        for i in range(len(arr)):
            longest = max(longest, hmap[arr[i] - difference] + 1)
            hmap[arr[i]] = hmap[arr[i] - difference] + 1
        return longest