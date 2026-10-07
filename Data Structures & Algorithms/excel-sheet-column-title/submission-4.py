class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        results = []
        while(columnNumber > 26):
            results.append(columnNumber % 26)
            columnNumber = columnNumber // 26
        results.append(columnNumber)
        # print(results, t, ta)
        for r in results:
            ans = chr(ord('A') + r - 1) + ans
        return ans
                    