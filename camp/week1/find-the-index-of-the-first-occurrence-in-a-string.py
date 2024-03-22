class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        a = 31
        m = (10**9)+7
        precomp = 0
        find = 0
        n = len(needle)
        for i in range(n):
            val = ord(needle[i]) - ord("a")+1
            c = ord(haystack[i]) - ord("a")+1
            find+=(a**(n-i))*c
            precomp+=(a**(n-i))*val
        precomp%=m
        find%=m
        
        print(precomp,find)
        #sliding window to find 
        l = 0
        n = len(needle)
        for r in range(len(haystack)):
   
            if r-l+1 > n:
                find+= ord(haystack[r]) - ord("a")+1
                find*=a
                remove = ord(haystack[l]) - ord("a")+1
                find-=(a**(n+1))*remove
                l+=1
            
         
            if r-l+1 == n:
                
                if find%m == precomp:
                    return l
        return -1
            
