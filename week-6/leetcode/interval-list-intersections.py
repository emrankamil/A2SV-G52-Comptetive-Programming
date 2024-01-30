class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 , p2 = 0, 0
        result = []
        while p1 < len(firstList) and p2 < len(secondList):
            if firstList[p1][0] > secondList[p2][1]:
                p2 += 1
            elif secondList[p2][0]>firstList[p1][1]:
                p1 += 1
            else:
                intr = [max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1], secondList[p2][1])]
                if firstList[p1][1] > secondList[p2][1]:
                    firstList[p1][0] = secondList[p2][1]
                    p2 += 1
                else:
                    secondList[p2][0] = firstList[p1][1]
                    p1 += 1
                result.append(intr)
        return result