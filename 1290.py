# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        num = ''
        cur = head
        while cur is not None:
            num += str(cur.val)
            cur = cur.next
        return int(num, 2)
