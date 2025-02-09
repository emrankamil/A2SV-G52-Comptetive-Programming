# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        mapp = {}
        for num in nums:
            if num not in mapp:
                mapp[num] = 1

        max_seq = 1
        for num in mapp:
            if mapp[num] == -1:
                continue
            cur = num
            while cur+1 in mapp and mapp[cur+1] != -1:
                mapp[num] += mapp[cur+1]
                mapp[cur+1] = -1 # -1 means it have been checked
                cur += 1
            max_seq = max(max_seq, mapp[num])

        return max_seq