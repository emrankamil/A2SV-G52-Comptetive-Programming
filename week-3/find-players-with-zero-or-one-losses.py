class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        loosers = {}
        for match in matches:
            winners.add(match[0])
            if match[1] in loosers:
                loosers[match[1]] += 1
            else:
                loosers[match[1]] = 1
        
        allWinners = []
        for i in winners:
            if i not in loosers:
                allWinners.append(i)
        allLoosers = []
        for i in loosers:
            if loosers[i] == 1:
                allLoosers.append(i)


        return [sorted(allWinners), sorted(allLoosers)]
        

        