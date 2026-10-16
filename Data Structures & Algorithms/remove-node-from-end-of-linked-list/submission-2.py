# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tot = 0
        cur = head
        while cur:
            tot += 1
            cur = cur.next
        target = tot - n
        cur = head.next
        prev = head
        for i in range(target-1):
            prev = cur
            cur = cur.next
        if cur and target != 0:
            prev.next = cur.next
        else:
            return cur
        return head