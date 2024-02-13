# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        count = 0
        while head:
            decimal = 2*decimal +  head.val
            head = head.next
        return decimal