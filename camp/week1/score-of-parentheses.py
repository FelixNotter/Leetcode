class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        balanced = 0
        for i in range(len(s)):
            if s[i] == "(":
                balanced+=1
            else:
                balanced-=1
                if s[i-1] == "(":
                    score+=2**balanced
        return score

        
            