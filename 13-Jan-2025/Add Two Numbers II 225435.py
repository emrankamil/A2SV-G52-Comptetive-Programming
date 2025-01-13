# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        head = ListNode()
        carry = 0
        while stack1 or stack2:
            a, b = 0, 0
            if stack1: a = stack1.pop()
            if stack2: b = stack2.pop()
            summ = a + b + carry
            head.val = summ%10
            carry = summ//10
            prev = head
            head = ListNode()
            head.next = prev
        if carry:
            head.val = carry
            return head
        return head.next