class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        leftRightRange = {i for i in range(left, right+1)}

        for singleRange in ranges:
            rangeSet = {i for i in range(singleRange[0],singleRange[1]+1)}
            leftRightRange.difference_update(rangeSet)
            if not leftRightRange:
                return True
        return False