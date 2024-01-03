class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seeker=1
        placeholder=0
        while seeker<len(nums):
            if nums[seeker]==nums[placeholder]:
                seeker+=1

            else:
                nums[placeholder+1]=nums[seeker]
                placeholder+=1
            if seeker==len(nums):
                for i in range(placeholder+1,len(nums)):
                    nums[i]= '_'

        return placeholder+1