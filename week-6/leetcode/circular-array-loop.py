class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checkSet = set()
        slow, fast, n = 0, 0, len(nums)
        check = False

        while fast * nums[fast] >= 0:
            if check:
                slow = (slow+nums[slow])%n
                check = not check
            fast = (fast+nums[fast])%n
            
            if slow == fast:
                # fast = (fast+nums[fast])%n
                # while slow != fast:
                #     if slow*fast < 0:
                #         return False
                #     fast = (fast+nums[fast])%n
                return True
            x = (slow, fast)
            if x in checkSet:
                return False
            else:
                checkSet.add(x)
       
        return False

# here we are using the array it self when we jump from one 
# index to the other

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)

        for i in range(n):
            # Skip if already visited
            if nums[i] == 0: continue

            fast = slow = i
    
            # Condition: fast and fast_next and fast_next_next travel at same direction (either positive or negative)
            next_fast = (fast + nums[fast]) % n
            while nums[fast] * nums[next_fast] > 0 and \
                  nums[next_fast] * nums[(next_fast + nums[next_fast]) % n]> 0:
                fast = (next_fast + nums[next_fast]) % n
                next_fast = (fast + nums[fast]) % n
                slow = (slow + nums[slow]) % n
                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break 
                    return True
            
            # Condition: slow and slow_next travel at same direction (either positive or negative)
            # Mark 'visited' by assigning 0
            slow = i
            while slow * nums[(slow + nums[slow]) % n] > 0:
                next_slow = (slow + nums[slow]) % n # preserve next value
                nums[slow] = 0 # mark 'visited'
                slow = next_slow # move to next
            
        return False