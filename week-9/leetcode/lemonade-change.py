class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                mp[5] += 1
            elif bill == 10:
                mp[10] += 1
                if mp[5]:
                    mp[5] -= 1
                else:
                    return False
            else:
                if mp[10]:
                    mp[10] -= 1
                    if mp[5]:
                        mp[5]-= 1
                    else:
                        return False
                elif mp[5]>=3:
                    mp[5] -= 3
                else:
                    return False
        return True