class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        s = set()
        for i in nums1:
            s.add(i)
        for i in nums2:
            if i in s:
                s.remove(i)
                ans.append(i)
        return ans