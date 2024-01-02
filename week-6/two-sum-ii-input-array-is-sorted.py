class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer1=0
        pointer2=len(numbers)-1
        while pointer1<pointer2:
            if numbers[pointer1] + numbers[pointer2]==target:
                return [pointer1+1,pointer2+1]
            elif numbers[pointer1] + numbers[pointer2] < target:
                pointer1+=1
            else:
                pointer2-=1