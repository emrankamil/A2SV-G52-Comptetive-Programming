class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        i = 0
        total = 1
        for i in range(len(points)-1):
            if points[i][1]<points[i+1][0]:
                total+= 1
            elif points[i][1]<points[i+1][1]:
                points[i+1][1] = points[i][1]

        return total
