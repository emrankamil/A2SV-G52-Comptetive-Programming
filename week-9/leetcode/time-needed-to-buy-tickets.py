class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0

        for i,ticket in enumerate(tickets):
            if ticket < tickets[k]:
                result += ticket
            else:
                if i > k:
                    result += tickets[k]-1
                else:
                    result += tickets[k]

        return result
        
        