# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        for i in range(len(intervals)):
            if i == len(intervals) - 1 or intervals[i+1][0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])

        return result