class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = True
        second = True
        num1 = edges[0][0]
        num2 = edges[0][1]
        for num in edges:
            if num1 not in num:
                first = False
            elif num2 not in num:
                second = False
        if first:
            return num1
        return num2