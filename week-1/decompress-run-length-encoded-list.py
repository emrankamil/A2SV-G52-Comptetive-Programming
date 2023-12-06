class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(1,len(nums),2):
            output.extend([nums[i]]*nums[i-1])

        return output