# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode()
        larger_head = ListNode()
        smaller_node = smaller_head
        larger_node = larger_head

        while head:
            if head.val < x:
                smaller_node.next = head
                smaller_node = smaller_node.next
            else:
                larger_node.next = head
                larger_node = larger_node.next
            head = head.next

        larger_node.next = None  
        smaller_node.next = larger_head.next  

        return smaller_head.next

        