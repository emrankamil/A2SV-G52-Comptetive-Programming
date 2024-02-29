# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        beforLeft = dummy_node
        
        for i in range(left - 1):
            beforLeft = beforLeft.next
        leftNode = beforLeft.next
        
        prevNode = None
        firstleft = leftNode
        for k in range(right - left + 1):
            nextNode = leftNode.next
            leftNode.next = prevNode
            prevNode = leftNode
            leftNode = nextNode
            
        beforLeft.next = prevNode
        firstleft.next = leftNode
        
        return dummy_node.next
        
            
        