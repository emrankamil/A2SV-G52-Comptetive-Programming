class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance_to_target = abs(target[0])+abs(target[1]) # ie from the origin

        for ghost in ghosts:
            if abs(target[0]-ghost[0])+abs(target[1]-ghost[1]) <= distance_to_target:
                return False

        return True