# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = defaultdict(int)
        longest = 0
        left, right = 0, 0
        while right < len(s):
            while mapp[s[right]] and left < right:
                mapp[s[left]] -= 1
                left += 1

            mapp[s[right]] += 1
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest