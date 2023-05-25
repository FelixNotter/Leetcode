class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        res = 0 
        for l in s:
            if l == letter:
                res += 1
        return int((res/len(s) * 100) // 1)
