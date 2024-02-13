# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prevNode = None
        right = head

        while right.next:
            right.prev = prevNode
            prevNode = right
            right = right.next

        right.prev = prevNode
        while right != head:
            if right.val != head.val:
                return False
            head = head.next
            right = right.prev
        return True
