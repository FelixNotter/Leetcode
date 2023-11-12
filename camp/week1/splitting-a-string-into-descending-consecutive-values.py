class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i,curr):
            if i == len(s):
                return len(curr) >= 2
            for j in range(i,len(s)):
                val = int(s[i:j+1])
                if (not curr) or (curr[-1] - val) == 1:
                    curr.append(val)
                    if backtrack(j+1,curr):
                        return True
                    curr.pop()
            return False

        return backtrack(0,[])
  

        