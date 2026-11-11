"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        needsNode = defaultdict(list)

        def solve(node):
            nonlocal oldToNew
            nonlocal needsNode

            if not node:
                return None
            copy = Node(x=node.val)
            oldToNew[node] = copy
            if node.random:
                if node.random in oldToNew:
                    copy.random = oldToNew[node.random]
                else:
                    needsNode[node.random].append(copy)

            if node in needsNode:
                for u in needsNode[node]:
                    u.random = copy
            
            copy.next = solve(node.next)
            return copy

        return solve(head)
