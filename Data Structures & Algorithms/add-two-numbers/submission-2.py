# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ans = ListNode()
        cur = ans
        cur.val = 0
        while l1 and l2:
            sumc = l1.val + l2.val
            cur.val += sumc % 10
            l1 = l1.next
            l2 = l2.next
            if (l1 or l2) or sumc >= 10:
                cur.next = ListNode()
                if sumc >= 10:
                    cur.next.val = 1
                cur = cur.next
        if l1:
            while l1:
                cur.val += l1.val
                l1 = l1.next
                if l1 or cur.val >= 10:
                    cur.next = ListNode()
                    if cur.val >= 10:
                        cur.next.val = 1
                        cur.val %= 10
                    cur = cur.next
        if l2:
            while l2:
                cur.val += l2.val
                l2 = l2.next
                if l2 or cur.val >= 10:
                    cur.next = ListNode()
                    if cur.val >= 10:
                        cur.next.val = 1
                        cur.val %= 10
                    cur = cur.next
        return ans

