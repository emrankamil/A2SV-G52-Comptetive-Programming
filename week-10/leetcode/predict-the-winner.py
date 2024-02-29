class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        s = {}
        def turn(left, right, player):
            if (left,right,player) in s:
                return s[(left,right,player)]
            if left == right:
                return nums[left]
            if player:
                option1 = nums[left]+turn(left+1,right,not player)
                option2 = nums[right] + turn(left, right-1, not player)
                s[(left,right,player)] = max(option1, option2)
              
            else:
                option1 = -nums[left]+turn(left+1,right,not player)
                option2 = -nums[right] + turn(left, right-1, not player)
                s[(left,right,player)] = min(option1, option2)

            return s[(left,right,player)]

        return turn(0, len(nums)-1,True) >= 0
