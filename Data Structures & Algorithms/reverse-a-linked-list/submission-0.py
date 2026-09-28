# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, i = None, head
        while i:
            next_val = i.next
            i.next = prev
            prev = i
            i = next_val
        
        return prev
            