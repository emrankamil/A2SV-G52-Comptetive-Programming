class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_seats = [0]*n
        for booking in bookings:
            left = booking[0]-1
            right = booking[1]
            total_seats[left] += booking[2]
            if right < n:
                total_seats[right] -= booking[2]
        
        for i in range(1,n):
            total_seats[i] +=  total_seats[i-1]
            
        return total_seats