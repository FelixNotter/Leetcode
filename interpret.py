class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        hmap = {
            2:"o",
            4:"al",
        }
        res = []
        for char in command:
            if char != "G":
                stack.append(char)
            if char == ")":
                res.append(hmap[len(stack)])
                for i in range(len(stack)):
                    stack.pop()
            
            if char == "G":
                res.append("G")
            
        return "".join(res)
