class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0 , len(skill)-1
        chemistry = 0

        while j > i:
            if skill[i]+skill[j] == skill[i+1]+skill[j-1]:
                chemistry += skill[i]*skill[j]
                i += 1
                j -= 1
            else:
                return -1
        return chemistry

        