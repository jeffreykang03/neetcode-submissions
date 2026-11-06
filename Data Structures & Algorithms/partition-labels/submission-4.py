class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        curl = 1
        pos = 0
        # indicies = {}
        # for i, ch in enumerate(s):
        #     indicies[i] = ch
        while pos < len(s):
            last = len(s) - 1
            need = {}
            while s[last] != s[pos]:
                if s[last] not in need:
                    need[s[last]] = last
                last -= 1
            substr = s[pos:last+1]
            print(substr, need)
            i = 0
            while i < len(substr):
                ch = substr[i]
                # if ch in need:
                #     print(ch, need[ch], last)
                if ch in need and need[ch] > last:
                    substr = s[pos:need[ch]+1]
                    last = need[ch]
                i += 1
            print(substr)
            ans.append(last-pos+1)
            pos = last+1
        return ans

