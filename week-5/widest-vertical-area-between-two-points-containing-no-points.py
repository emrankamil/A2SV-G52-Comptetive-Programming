class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        array = [i[0] for i in points]
        array.sort()
        maxWidth = 0
        for i in range(len(array)-1):
            maxWidth = max(array[i+1]-array[i], maxWidth)

        return maxWidth

        