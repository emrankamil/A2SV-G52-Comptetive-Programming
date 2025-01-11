# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sumList = ListNode()
        carry = 0
        current = sumList
        
        while l1 or l2:
            result = carry
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            current.next = ListNode(result % 10)
            current = current.next
            carry = result//10
        if carry:
            current.next = ListNode(carry)
            
        return sumList.next
                