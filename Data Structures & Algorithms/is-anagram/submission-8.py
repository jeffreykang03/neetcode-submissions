class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = {}
        for c in s:
            if(not(c in st.keys())):
                st[c] = 1
            else:
                st[c] = st[c] + 1
        for c in t:
            if(not(c in st.keys())):
                return False;
            if(st[c] == 1):
                st.pop(c)
            else:
                st[c] = st[c] - 1
        return not(st)
        