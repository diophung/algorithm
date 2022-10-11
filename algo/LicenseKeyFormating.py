class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        firstDashIndex = s.index("-")
        s = s.replace("-", "").upper()
        newKey = ""
        l = len(s)
        idx = 0
        if firstDashIndex <= k:
            # include dash
            newKey += s[0:firstDashIndex] + "-"
            idx = firstDashIndex

        ct = 0
        while idx < l:
            ct += 1
            if ct % k == 0:
                newKey += "-"
                ct = 0
            newKey += s[idx]
            idx += 1

        return newKey


sln = Solution()
print(sln.licenseKeyFormatting("123-2e-9-w", 2))

