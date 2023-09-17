class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split("/")
     
        for directory in directories:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == ".":
                continue
            else:
                if directory:
                    stack.append(directory)
        print(stack)
        return "/"+"/".join(stack)
    

        