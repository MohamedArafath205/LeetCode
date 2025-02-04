# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail, len_ = head, 1
        while tail.next:
            tail = tail.next
            len_ += 1
        
        k = k % len_
        if k == 0:
            return head

        cur = head
        for i in range(len_-k-1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
