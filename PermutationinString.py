class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = [0]*26
        for char in s1:
            window[ord(char)-ord("a")]+=1
        count = [0]*26
        l = 0
        for r in range(len(s2)):
            idx = ord(s2[r])-ord("a")
            count[idx]+=1
            while count[idx] > window[idx]:
                count[ord(s2[l])-ord("a")]-=1
                l+=1
            if count == window:
                return True
        return False

            
