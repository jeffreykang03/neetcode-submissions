# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(h1, h2):
            dummy = ListNode()
            cur = dummy
            p1 = h1
            p2 = h2
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            if p1:
                cur.next = p1
            else:
                cur.next = p2
            return dummy.next
        
        def solve(l, r):
            if r == l:
                return lists[r]
            mid = l + (r-l) // 2
            return mergetwo(solve(l, mid), solve(mid+1, r))
        
        if not lists:
            return None
        return solve(0, len(lists)-1)


