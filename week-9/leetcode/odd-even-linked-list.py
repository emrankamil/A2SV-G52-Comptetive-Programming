# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd, even = head, head.next
        head2 = even
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even= even.next
        odd.next = head2
        return head
            