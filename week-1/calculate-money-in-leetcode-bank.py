class Solution:
    def totalMoney(self, n: int) -> int:
        floor = n//7
        modulo = n%7
        #arithmetic sum : n/2(firstElement + lastElement)
        full_cycle_sum = (floor*28)+((floor-1)*(7+(floor-1)*7))//2
        modulo_cycle_sum = modulo*((floor+1 )+ (floor+modulo))//2

        return full_cycle_sum + modulo_cycle_sum