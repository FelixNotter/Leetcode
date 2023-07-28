class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        r = 0
        n = len(s)
        seen = set()
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                print(seen)
                r+=1    
            else:
                seen.remove(s[l])
                l +=1
                
            length = max(length,len(seen))
        return length 

        
        
