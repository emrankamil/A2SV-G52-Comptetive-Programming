# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            if cur.next.val:
                cur.val += cur.next.val
                cur.next = cur.next.next
            else:
                if not cur.next.next:
                    cur.next = None
                else: cur = cur.next
        return head
