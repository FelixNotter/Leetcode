class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and (stack[-1][0] == char) and (stack[-1][1] == k-1):
                for _ in range(k-1):
                    stack.pop()
                
            else:
                if stack and stack[-1][0] == char:
                    stack.append((char,stack[-1][1]+1))
                else:
                    stack.append((char,1))
        res = []
        for char in stack:
            res.append(char[0])
        return "".join(res)
        