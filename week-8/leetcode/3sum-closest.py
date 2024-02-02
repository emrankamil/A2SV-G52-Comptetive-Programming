class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = float('inf')
        s= nums[0]+nums[1]+nums[-1]
        min_distance = abs(s-target)

        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:continue
            
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i]+nums[left]+nums[right] 
                if s == target:
                    return target
                if abs(target-s) < abs(target-ans):
                    ans = s
                
                if s < target:
                    left += 1
                else:
                    right -= 1

        return ans