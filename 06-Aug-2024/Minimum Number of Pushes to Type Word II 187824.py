# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = [0] * 26
        rst = 0
        for char in word:
            counter[ord(char) - ord("a")] += 1
        counter.sort(reverse=True)

        for i in range(len(counter)):
            rst += (i//8 + 1) * counter[i]
        
        return rst