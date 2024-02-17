# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.checked = False

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1, head2 = headA, headB
        while head1 and head2:
            head1 = head1.next
            head2 = head2.next
        
        while head1:
            head1 = head1.next
            headA = headA.next
        while head2:
            head2 = head2.next
            headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

        