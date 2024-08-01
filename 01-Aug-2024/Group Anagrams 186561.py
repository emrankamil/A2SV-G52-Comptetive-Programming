# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = {}
        for i in range(len(strs)):
            sortedStr = tuple(sorted(strs[i]))
            if sortedStr in container:
                container[sortedStr].append(strs[i])
            else:
                container[sortedStr] = [strs[i]]
        
        rst = []
        for i in container:
            rst.append(container[i])

        return rst
        