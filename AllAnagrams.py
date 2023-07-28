class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        sCount = [0]*26
        res  = []
        pCount = [0]*26
        for char in p:
            pCount[ord(char)-ord("a")] +=1

        for r in range(len(s)):
            sCount[ord(s[r])-ord("a")] += 1
            if r-l+1 > len(p):
                sCount[ord(s[l])-ord("a")] -= 1
                l+=1
            if r-l+1 == len(p):
                if sCount == pCount:
                    res.append(l)
        return res
