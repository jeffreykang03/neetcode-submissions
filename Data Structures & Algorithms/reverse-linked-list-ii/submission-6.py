class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        before = dummy

        for _ in range(left - 1):
            before = before.next

        start = before.next
        cur = start
        nex = cur.next

        for _ in range(right - left):
            temp = cur
            cur = nex
            nex = nex.next
            cur.next = temp

        before.next = cur
        start.next = nex

        return dummy.next