class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sort the list in ascending order
        i, j = 0, len(people) - 1
        boats = 0
        
        while j >= i:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1

        return boats