# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = ListNode()
        left.next = head
        right = head
        check = False
        while right.next:
            n -= 1
            if n <= 0:
                left = left.next
                check = True
            right = right.next
        left.next = left.next.next
        if check:
            return head
        return left.next