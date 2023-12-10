class Solution:
    def arrayChange(self, nums: List[int], ops: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i

        for i in range(len(ops)):
            currele = ops[i][0]
            newele = ops[i][1]
            nums[mp[currele]] = newele
            mp[newele] = mp[currele]

        return nums
