from collections import Counter
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        minHeight = min(heights)
        counter = [0]*(max(heights)-min(heights)+1)
        for i in range(len(names)):
            counter[heights[i]-minHeight] = names[i]
        rst = []
        for i in range(len(counter)-1,-1,-1):
            if counter[i] != 0:
                rst.append(counter[i])

        return rst