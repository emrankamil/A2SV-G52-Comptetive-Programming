class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
Hints I used: 
1 - But, they're only asking for consecutive array such that the difference between each adjecent element is exactly 1( From the discussion) 
        """
        setOfNums = set(nums)
        counter = {}
        maxSequence = 0
        for num in nums:
#For every num existed in set, try to probe to right to see if following numbers are also in set, and record longest possible sequence.
            if num-1 not in setOfNums: 
                counter[num] = 1
                nextSequence = num + 1
                while nextSequence in setOfNums:
                    counter[num] += 1
                    nextSequence += 1
                maxSequence = max(maxSequence, counter[num])

        return maxSequence

        