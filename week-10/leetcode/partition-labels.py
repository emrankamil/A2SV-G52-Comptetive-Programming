class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i in range(len(s)-1,-1,-1):
            if s[i] not in lastIndex:
                lastIndex[s[i]]=i

        counter = 0
        end = 0
        output = []

        for index,val in enumerate(s):
            counter += 1
            if lastIndex[val] >= end:
                end = lastIndex[val]
                start = index
            if index == end:
                output.append(counter)
                counter = 0

        return (output)
