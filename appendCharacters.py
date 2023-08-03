class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        for r in range(len(s)):
            if l < len(t) and s[r] == t[l]:
                l+=1
        if l < len(t):
            return len(t) - l
        return 0
