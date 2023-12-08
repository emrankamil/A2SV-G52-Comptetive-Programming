class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        if start < destination:
            distance1 = sum(distance[start:destination])
        else:
            distance1 = sum(distance[destination:start])

     
        return min(distance1, sum(distance)-distance1)