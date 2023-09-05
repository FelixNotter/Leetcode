class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        found=False
        for k,v in count.items():
            if v % 2 == 0:
                res+=v
            else:
                res+=v-1
                found = True
        return res+1 if found else res

        
